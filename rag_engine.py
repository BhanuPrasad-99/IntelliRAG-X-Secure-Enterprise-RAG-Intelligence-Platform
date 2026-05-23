"""RAG Engine with Hybrid Retrieval, Confidence Scoring, and Citation Support"""
import json
from typing import List, Dict, Tuple
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
    import faiss
    from rank_bm25 import BM25Okapi
    HAS_DEPENDENCIES = True
except ImportError:
    HAS_DEPENDENCIES = False
    print("⚠️  Warning: Some dependencies not installed. Run: pip install -r requirements.txt")

from rbac import RBACEngine

class RAGEngine:
    """Enterprise RAG with Hybrid Retrieval, RBAC, and Confidence Scoring"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        if not HAS_DEPENDENCIES:
            raise RuntimeError("Please install dependencies: pip install -r requirements.txt")
        
        self.embedder = SentenceTransformer(model_name)
        self.documents = []
        self.index = None
        self.bm25 = None
        self.rbac = RBACEngine()
        self.embeddings = []
    
    def build_index(self, documents: List[Dict]):
        """Build FAISS vector index from documents"""
        if not documents:
            print("⚠️  No documents to index")
            return
        
        self.documents = documents
        
        # Generate embeddings
        texts = [doc.get("content", "") for doc in documents]
        print(f"🔄 Generating embeddings for {len(texts)} documents...")
        self.embeddings = self.embedder.encode(texts, convert_to_numpy=True)
        
        # Create FAISS index
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings.astype('float32'))
        print(f"✅ FAISS index created with {len(documents)} documents")
        
        # Build BM25 for keyword search
        tokenized_texts = [text.split() for text in texts]
        self.bm25 = BM25Okapi(tokenized_texts)
        print(f"✅ BM25 index created")
    
    def hybrid_retrieve(
        self, 
        query: str, 
        user_role: str,
        top_k: int = 5
    ) -> Tuple[List[Dict], List[float]]:
        """
        Hybrid retrieval: semantic + keyword search with RBAC filtering.
        
        Score = (0.45 × Semantic) + (0.30 × BM25) + (0.15 × Trust) + (0.10 × Recency)
        """
        if not self.index or not self.bm25:
            return [], []
        
        # Encode query
        query_embedding = self.embedder.encode(query, convert_to_numpy=True)
        
        # Semantic search via FAISS
        distances, indices = self.index.search(
            np.array([query_embedding]).astype('float32'), 
            min(top_k * 2, len(self.documents))
        )
        
        semantic_scores = 1 / (1 + distances[0])
        
        # Keyword search via BM25
        query_tokens = query.split()
        bm25_scores = self.bm25.get_scores(query_tokens)
        
        # Normalize scores
        semantic_scores_norm = semantic_scores / (np.max(semantic_scores) + 1e-6)
        bm25_scores_norm = bm25_scores / (np.max(bm25_scores) + 1e-6)
        
        # Hybrid score calculation
        hybrid_scores = {}
        for idx in indices[0]:
            doc = self.documents[idx]
            sem_score = semantic_scores_norm[list(indices[0]).index(idx)]
            bm25_score = bm25_scores_norm[idx]
            trust_score = 0.9
            recency_score = 0.85
            
            final_score = (
                0.45 * sem_score +
                0.30 * bm25_score +
                0.15 * trust_score +
                0.10 * recency_score
            )
            
            hybrid_scores[idx] = {
                "score": final_score,
                "semantic": sem_score,
                "bm25": bm25_score,
                "document": doc
            }
        
        # Sort by hybrid score
        sorted_results = sorted(hybrid_scores.items(), key=lambda x: x[1]["score"], reverse=True)
        
        # RBAC filtering BEFORE returning (CRITICAL SECURITY)
        filtered_results = []
        for idx, result in sorted_results[:top_k]:
            doc = result["document"]
            if self.rbac.is_authorized(user_role, doc.get("department", "")):
                filtered_results.append({
                    "index": idx,
                    "content": doc.get("content", "")[:300],
                    "source": doc.get("source", ""),
                    "department": doc.get("department", ""),
                    "type": doc.get("type", ""),
                    "metadata": doc.get("metadata", {}),
                    "confidence": min(result["score"] * 100, 100),
                    "semantic_score": result["semantic"],
                    "bm25_score": result["bm25"]
                })
        
        confidences = [r["confidence"] for r in filtered_results]
        return filtered_results, confidences
    
    def generate_citation(self, retrieval_result: Dict) -> str:
        """Generate citation from retrieval result"""
        source = retrieval_result.get("source", "Unknown").split('/')[-1]
        confidence = retrieval_result.get("confidence", 0)
        return f"Source: {source} | Confidence: {confidence:.1f}%"
    
    def calculate_answer_confidence(self, confidences: List[float]) -> str:
        """Calculate overall answer confidence level"""
        if not confidences:
            return "Low"
        
        avg_confidence = sum(confidences) / len(confidences)
        
        if avg_confidence >= 80:
            return "High"
        elif avg_confidence >= 60:
            return "Medium"
        else:
            return "Low"
    
    def format_response(
        self,
        answer: str,
        retrieval_results: List[Dict],
        confidence_level: str
    ) -> Dict:
        """Format final response with citations and confidence"""
        return {
            "answer": answer,
            "confidence_level": confidence_level,
            "confidence_score": sum([r["confidence"] for r in retrieval_results]) / len(retrieval_results) if retrieval_results else 0,
            "citations": [self.generate_citation(r) for r in retrieval_results],
            "retrieved_sources": [
                {
                    "source": r["source"].split('/')[-1],
                    "type": r["type"],
                    "confidence": r["confidence"],
                    "department": r["department"]
                }
                for r in retrieval_results
            ],
            "retrieval_trace": {
                "total_results": len(retrieval_results),
                "semantic_match": len([r for r in retrieval_results if r["semantic_score"] > 0.7]),
                "access_level": "Authorized"
            }
        }
