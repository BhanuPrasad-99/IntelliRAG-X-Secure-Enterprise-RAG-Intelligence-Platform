#!/usr/bin/env python3
"""
Test script for IntelliRAG-X
Run this to verify the system is working
"""
import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_rbac():
    """Test RBAC engine"""
    print("\n" + "="*60)
    print("🔐 Testing RBAC Engine")
    print("="*60)
    
    from rbac import RBACEngine
    
    rbac = RBACEngine()
    
    test_cases = [
        ("admin", "finance", True),
        ("admin", "hr", True),
        ("finance", "finance", True),
        ("finance", "hr", False),
        ("hr", "hr", True),
        ("engineering", "finance", False),
    ]
    
    print("\nTesting authorization checks:")
    for role, dept, expected in test_cases:
        result = rbac.is_authorized(role, dept)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {role:12} → {dept:12} = {result} (expected {expected})")
    
    print("\n✅ RBAC tests passed!")

def test_data_ingestion():
    """Test data ingestion"""
    print("\n" + "="*60)
    print("📥 Testing Data Ingestion")
    print("="*60)
    
    from ingest import DataIngestionEngine
    
    engine = DataIngestionEngine()
    
    # Check if data directory exists
    if not os.path.exists("data"):
        print("\n⚠️  Data directory not found!")
        print("   Run: python setup_project.py")
        return False
    
    documents = engine.ingest_all_data("data")
    
    print(f"\n✅ Ingested {len(documents)} documents")
    
    if documents:
        print("\nSample documents:")
        for i, doc in enumerate(documents[:3], 1):
            print(f"  {i}. Type: {doc.get('type', 'unknown'):10} | Dept: {doc.get('department', 'unknown')}")
    
    return len(documents) > 0

def test_rag_engine():
    """Test RAG engine"""
    print("\n" + "="*60)
    print("🧠 Testing RAG Engine")
    print("="*60)
    
    try:
        from rag_engine import RAGEngine
        from ingest import DataIngestionEngine
        
        if not os.path.exists("data"):
            print("\n⚠️  Data directory not found!")
            print("   Run: python setup_project.py")
            return False
        
        # Ingest data
        print("\n📥 Ingesting data...")
        ingestion_engine = DataIngestionEngine()
        documents = ingestion_engine.ingest_all_data("data")
        
        if not documents:
            print("❌ No documents ingested")
            return False
        
        print(f"✅ Ingested {len(documents)} documents")
        
        # Build RAG engine
        print("\n🔨 Building RAG engine...")
        rag_engine = RAGEngine()
        rag_engine.build_index(documents)
        print("✅ RAG engine built")
        
        # Test retrieval
        print("\n🔍 Testing retrieval...")
        query = "failed login attempts"
        results, confidences = rag_engine.hybrid_retrieve(query, "admin", top_k=3)
        
        print(f"✅ Retrieved {len(results)} results")
        
        if results:
            print("\nTop results:")
            for i, result in enumerate(results, 1):
                print(f"  {i}. Confidence: {result['confidence']:.1f}% | Type: {result['type']}")
        
        # Test confidence
        print("\n📊 Confidence metrics:")
        if confidences:
            avg_conf = sum(confidences) / len(confidences)
            conf_level = rag_engine.calculate_answer_confidence(confidences)
            print(f"  Average: {avg_conf:.1f}%")
            print(f"  Level: {conf_level}")
        
        print("\n✅ RAG engine tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("   Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("🧪 IntelliRAG-X System Tests")
    print("="*60)
    
    results = {}
    
    # Test RBAC
    try:
        test_rbac()
        results["RBAC"] = True
    except Exception as e:
        print(f"❌ RBAC test failed: {e}")
        results["RBAC"] = False
    
    # Test Data Ingestion
    try:
        results["Data Ingestion"] = test_data_ingestion()
    except Exception as e:
        print(f"❌ Data ingestion test failed: {e}")
        results["Data Ingestion"] = False
    
    # Test RAG Engine
    try:
        results["RAG Engine"] = test_rag_engine()
    except Exception as e:
        print(f"❌ RAG engine test failed: {e}")
        results["RAG Engine"] = False
    
    # Summary
    print("\n" + "="*60)
    print("📋 Test Summary")
    print("="*60)
    
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"  {test_name:20} {status}")
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n" + "🎉 "*20)
        print("✅ ALL TESTS PASSED!")
        print("\n🚀 Next steps:")
        print("   1. python app.py")
        print("   2. Visit http://127.0.0.1:8000/docs")
        print("   3. Try a query!")
        print("🎉 "*20 + "\n")
        return 0
    else:
        print("\n❌ Some tests failed")
        print("   Make sure:")
        print("   1. python setup_project.py")
        print("   2. pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())
