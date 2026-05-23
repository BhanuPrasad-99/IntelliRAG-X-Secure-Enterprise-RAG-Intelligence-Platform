#!/usr/bin/env python3
"""
IntelliRAG-X: One-Click Quick Start Guide
This file shows exactly what to do, step by step
"""

print("""
╔══════════════════════════════════════════════════════════════════╗
║          🚀 IntelliRAG-X Quick Start Guide                      ║
║     Enterprise RAG for SimplifyX Hiring Challenge               ║
╚══════════════════════════════════════════════════════════════════╝

Your complete production-grade RAG system is ready!

═══════════════════════════════════════════════════════════════════
STEP 1: Initialize Project & Create Sample Data
═══════════════════════════════════════════════════════════════════

Command:
    python setup_project.py

What it does:
  ✓ Creates data/logs/ directory
  ✓ Creates data/policies/ directory
  ✓ Creates sample security events JSON
  ✓ Creates sample audit events JSON
  ✓ Creates RBAC policy configuration

Expected output:
  ✅ Created: data/logs/security_logs.json
  ✅ Created: data/logs/audit_logs.json
  ✅ Created: data/policies/rbac.json
  🎉 Project setup complete!

═══════════════════════════════════════════════════════════════════
STEP 2: Install Python Dependencies
═══════════════════════════════════════════════════════════════════

Command:
    pip install -r requirements.txt

What it installs:
  • FastAPI - Web framework
  • SentenceTransformers - Embeddings
  • FAISS - Vector search
  • BM25 - Keyword search
  • Pydantic - Data validation
  • And more...

Expected time: 2-5 minutes
Expected output: Successfully installed...

═══════════════════════════════════════════════════════════════════
STEP 3: Run Tests (Optional but Recommended)
═══════════════════════════════════════════════════════════════════

Command:
    python test_system.py

What it tests:
  ✓ RBAC authorization checks
  ✓ Data ingestion
  ✓ RAG engine initialization
  ✓ Retrieval functionality

Expected output:
  ✅ RBAC tests passed!
  ✅ Data ingestion complete
  ✅ RAG engine ready
  🎉 ALL TESTS PASSED!

═══════════════════════════════════════════════════════════════════
STEP 4: Start the Server
═══════════════════════════════════════════════════════════════════

Command:
    python app.py

What it does:
  ✓ Initializes FastAPI server
  ✓ Ingests sample data
  ✓ Builds FAISS vector index
  ✓ Creates BM25 keyword index
  ✓ Starts server on port 8000

Expected output:
  🚀 Initializing IntelliRAG-X...
  ✅ Ingested 8 documents
  ✅ Built FAISS index
  ✅ Built BM25 index
  🎯 IntelliRAG-X Ready!
  INFO:     Uvicorn running on http://127.0.0.1:8000

═══════════════════════════════════════════════════════════════════
STEP 5: Access the API
═══════════════════════════════════════════════════════════════════

Open in your browser:
  🌐 http://127.0.0.1:8000/docs

You'll see the Swagger UI with all available endpoints:
  POST /query        - Main RAG query
  GET  /health       - Health check
  GET  /rbac/check   - Test RBAC
  GET  /system/info  - System info

═══════════════════════════════════════════════════════════════════
STEP 6: Test API Endpoints
═══════════════════════════════════════════════════════════════════

Health Check:
  curl http://127.0.0.1:8000/health

RBAC Authorization:
  curl "http://127.0.0.1:8000/rbac/check?user_role=finance&department=finance"

Main Query (Admin - Full Access):
  curl -X POST "http://127.0.0.1:8000/query" \\
    -H "Content-Type: application/json" \\
    -d '{
      "query": "Show failed login attempts",
      "user_role": "admin",
      "top_k": 5
    }'

Main Query (Finance - Limited Access):
  curl -X POST "http://127.0.0.1:8000/query" \\
    -H "Content-Type: application/json" \\
    -d '{
      "query": "Show failed login attempts",
      "user_role": "finance",
      "top_k": 5
    }'

═══════════════════════════════════════════════════════════════════
SYSTEM ARCHITECTURE
═══════════════════════════════════════════════════════════════════

User Query
    ↓
🔐 RBAC Authorization (CRITICAL!)
    ↓
Hybrid Retrieval (Semantic + Keyword)
    ↓
🔐 RBAC Filtering (Remove Unauthorized)
    ↓
Confidence Scoring
    ↓
Response with Citations
    ↓
Answer + Sources + Confidence Score

Key Advantage: RBAC is enforced BEFORE retrieval, not after!

═══════════════════════════════════════════════════════════════════
RBAC ROLES & PERMISSIONS
═══════════════════════════════════════════════════════════════════

admin:       Can access ALL departments
finance:     Can access ONLY finance department
hr:          Can access ONLY hr department
engineering: Can access ONLY engineering department

Test different roles to see access control in action!

═══════════════════════════════════════════════════════════════════
WHAT YOU GET
═══════════════════════════════════════════════════════════════════

✅ Production-Grade RAG System
  • Hybrid semantic + keyword retrieval
  • Enterprise-grade security (RBAC)
  • Confidence scoring for every response
  • Complete citation & traceability
  • Hallucination prevention

✅ Full Documentation
  • START_HERE.md - Overview
  • README_QUICK_START.md - 5-min guide
  • IMPLEMENTATION_GUIDE.md - Technical details
  • PROJECT_COMPLETE.md - Summary

✅ Working Code
  • FastAPI backend server
  • Vector search engine
  • Secure RBAC layer
  • Data ingestion pipeline
  • Comprehensive test suite

✅ Sample Data
  • Security event logs
  • Audit event logs
  • RBAC policy configuration

═══════════════════════════════════════════════════════════════════
ADDING YOUR OWN DATA
═══════════════════════════════════════════════════════════════════

1. Add logs to data/logs/yourfile.json:
   [
     {
       "timestamp": "2026-03-15T10:00:00Z",
       "department": "finance",
       "event": "Your Event",
       "details": "Event details"
     }
   ]

2. Add RBAC roles to data/policies/rbac.json

3. Restart server: python app.py

New data is automatically ingested!

═══════════════════════════════════════════════════════════════════
TROUBLESHOOTING
═══════════════════════════════════════════════════════════════════

❌ "No documents found"
   → Run: python setup_project.py

❌ "ModuleNotFoundError: faiss"
   → Run: pip install -r requirements.txt --force-reinstall

❌ "Port 8000 already in use"
   → Edit app.py, change port to 8001, restart

❌ "RBAC always returns False"
   → Check data/policies/rbac.json configuration

❌ "Tests fail"
   → Make sure python setup_project.py ran successfully
   → Make sure all dependencies installed

═══════════════════════════════════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════════════════════════════════

1. Run the quick start (above)
2. Test all API endpoints
3. Try different user roles
4. Add your own data
5. Customize as needed
6. Deploy to production (Docker ready!)

═══════════════════════════════════════════════════════════════════
KEY FILES
═══════════════════════════════════════════════════════════════════

Core System:
  app.py              - FastAPI server
  rag_engine.py       - Retrieval engine
  rbac.py             - Security layer
  ingest.py           - Data loading

Documentation:
  START_HERE.md                - Start here!
  README_QUICK_START.md        - Quick start
  IMPLEMENTATION_GUIDE.md      - Full guide
  PROJECT_COMPLETE.md          - Summary

Configuration:
  requirements.txt             - Python deps
  setup_project.py             - Initialize project

═══════════════════════════════════════════════════════════════════
WHAT THIS DEMONSTRATES FOR INTERVIEWS
═══════════════════════════════════════════════════════════════════

✅ Production Architecture
   - Layered design
   - Enterprise patterns
   - Scalable components

✅ Enterprise Security
   - RBAC as first-class citizen
   - Zero data leakage guarantee
   - Access control before retrieval

✅ AI Systems Knowledge
   - Hybrid retrieval algorithms
   - Confidence scoring
   - Hallucination prevention
   - Explainability & traceability

✅ Practical Implementation
   - Working backend
   - Real vector search
   - Actual scoring algorithms
   - Full test coverage

═══════════════════════════════════════════════════════════════════
🎉 YOU'RE ALL SET!
═══════════════════════════════════════════════════════════════════

Your system is ready to impress SimplifyX!

Quick recap:
1. python setup_project.py          (Initialize)
2. pip install -r requirements.txt  (Install deps)
3. python test_system.py            (Optional tests)
4. python app.py                    (Start server)
5. http://127.0.0.1:8000/docs      (Use API)

Built for SimplifyX Hiring Challenge 2026
Status: Production Ready ✅
Version: 1.0.0

Questions? See the full guides:
- START_HERE.md
- IMPLEMENTATION_GUIDE.md
- PROJECT_COMPLETE.md

🚀 Ready to get interview calls? Build, test, deploy, and submit!
""")

# Quick validation
import os
import sys

print("\n" + "="*60)
print("Checking your setup...")
print("="*60)

checks = {
    "app.py": "FastAPI server",
    "rag_engine.py": "RAG engine",
    "rbac.py": "RBAC security",
    "ingest.py": "Data ingestion",
    "requirements.txt": "Dependencies",
    "setup_project.py": "Setup script",
    "test_system.py": "Test suite"
}

all_good = True
for file, desc in checks.items():
    exists = "✅" if os.path.exists(file) else "❌"
    print(f"{exists} {file:25} - {desc}")
    if not os.path.exists(file):
        all_good = False

print("\n" + "="*60)
if all_good:
    print("✅ All files present! You're ready to go!")
    print("\nNext command: python setup_project.py")
else:
    print("❌ Some files missing. Make sure you're in d:\\simpilify X\\")
print("="*60 + "\n")
