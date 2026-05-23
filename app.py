"""FastAPI Backend for IntelliRAG-X Enterprise RAG System"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import sys

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ingest import DataIngestionEngine
from rag_engine import RAGEngine
from rbac import RBACEngine

# Initialize FastAPI app
app = FastAPI(
    title="IntelliRAG-X",
    description="Secure Multi-Source Enterprise RAG Assistant",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize engines
ingestion_engine = DataIngestionEngine()
rag_engine = None
rbac_engine = RBACEngine()

# Pydantic models
class QueryRequest(BaseModel):
    query: str
    user_role: str
    top_k: int = 5

class QueryResponse(BaseModel):
    answer: str
    confidence_level: str
    confidence_score: float
    citations: List[str]
    retrieved_sources: List[dict]
    retrieval_trace: dict

# Startup event
@app.on_event("startup")
async def startup_event():
    global rag_engine
    print("\n🚀 Initializing IntelliRAG-X...")
    
    # Find data directory
    data_dir = "data"
    if not os.path.exists(data_dir):
        data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    # Ingest data
    documents = ingestion_engine.ingest_all_data(data_dir)
    
    if documents:
        print(f"✅ Ingested {len(documents)} documents")
        rag_engine = RAGEngine()
        rag_engine.build_index(documents)
        print("🎯 IntelliRAG-X Ready!")
    else:
        print("⚠️  No documents found. Create data/logs and data/policies directories with JSON files.")
        rag_engine = None

# Health check
@app.get("/health")
async def health_check():
    return {
        "status": "healthy" if rag_engine else "initializing",
        "system": "IntelliRAG-X",
        "documents_indexed": len(rag_engine.documents) if rag_engine else 0,
        "version": "1.0.0"
    }

# Main query endpoint
@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    """
    Main RAG query endpoint with RBAC, hybrid retrieval, and confidence scoring.
    
    SECURITY: RBAC enforcement occurs BEFORE retrieval and BEFORE LLM generation
    to completely prevent unauthorized context exposure.
    """
    if not rag_engine:
        raise HTTPException(
            status_code=503,
            detail="RAG engine not initialized. Please check data directory."
        )
    
    try:
        # Validate user role
        valid_roles = ["admin", "finance", "hr", "engineering"]
        if request.user_role.lower() not in valid_roles:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid user role. Valid roles: {valid_roles}"
            )
        
        # Hybrid retrieval with RBAC filtering
        retrieval_results, confidences = rag_engine.hybrid_retrieve(
            query=request.query,
            user_role=request.user_role,
            top_k=request.top_k
        )
        
        # Check if sufficient authorized context available
        if not retrieval_results:
            answer = "Insufficient verified enterprise context available for this query."
            confidence_level = "Low"
            confidence_score = 0
            citations = []
            retrieved_sources = []
            retrieval_trace = {"access_level": "Authorized", "total_results": 0}
        else:
            # Simulate LLM-generated answer (grounded in retrieval results)
            answer = f"Based on enterprise data: {retrieval_results[0]['content']}..."
            confidence_level = rag_engine.calculate_answer_confidence(confidences)
            confidence_score = sum(confidences) / len(confidences) if confidences else 0
            citations = [rag_engine.generate_citation(r) for r in retrieval_results]
            retrieved_sources = [
                {
                    "source": r["source"].split('/')[-1],
                    "type": r["type"],
                    "confidence": r["confidence"],
                    "department": r["department"]
                }
                for r in retrieval_results
            ]
            retrieval_trace = {
                "total_results": len(retrieval_results),
                "semantic_match": len([r for r in retrieval_results if r["semantic_score"] > 0.7]),
                "access_level": "Authorized"
            }
        
        return QueryResponse(
            answer=answer,
            confidence_level=confidence_level,
            confidence_score=confidence_score,
            citations=citations,
            retrieved_sources=retrieved_sources,
            retrieval_trace=retrieval_trace
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# RBAC test endpoint
@app.get("/rbac/check")
async def rbac_check(user_role: str, department: str):
    """Check if user role can access department"""
    is_authorized = rbac_engine.is_authorized(user_role, department)
    return {
        "user_role": user_role,
        "department": department,
        "is_authorized": is_authorized
    }

# System info endpoint
@app.get("/system/info")
async def system_info():
    """Get system information"""
    return {
        "system": "IntelliRAG-X",
        "version": "1.0.0",
        "documents_indexed": len(rag_engine.documents) if rag_engine else 0,
        "supported_roles": ["admin", "finance", "hr", "engineering"],
        "features": [
            "Hybrid Semantic + Keyword Search",
            "Role-Based Access Control",
            "Confidence Scoring",
            "Citation Support",
            "Retrieval Traceability",
            "Hallucination Prevention",
            "Enterprise Security"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )
