# 🧠 IntelliRAG-X

## Secure Enterprise RAG Intelligence Platform

RBAC authorization is enforced BEFORE vector retrieval to guarantee zero unauthorized context exposure.

IntelliRAG-X is a production-oriented enterprise Retrieval-Augmented Generation (RAG) platform designed to securely retrieve and generate grounded responses across disconnected enterprise data silos.

The platform supports intelligent retrieval from:

* PDFs & enterprise documents
* SQL/CSV datasets
* JSON logs & alerts
* Audit records
* Operational datasets
* Access policies & metadata

while enforcing strict Role-Based Access Control (RBAC) to prevent unauthorized data exposure.

---

# 🚀 Features

## 🔐 Enterprise Security

* RBAC-aware retrieval
* Department-level access control
* Secure context filtering
* Unauthorized context prevention
* Enterprise-grade security architecture

## 🧠 Intelligent Retrieval

* Hybrid Search (Semantic + BM25)
* FAISS Vector Database
* Cross-source retrieval
* Query-aware routing
* Multi-source reasoning

## 📊 Explainable AI

* Confidence scoring
* Citation support
* Retrieval traceability
* Source attribution
* Explainable responses

## ⚡ Enterprise Architecture

* FastAPI backend
* Streamlit dashboard
* Modular architecture
* Scalable deployment design
* Production-oriented pipeline

---

# 🏗️ System Architecture

```text
User Query
    ↓
Authentication Layer
    ↓
RBAC Authorization Engine
    ↓
Query Understanding
    ↓
Hybrid Retrieval Engine
 ┌────────────────────┐
 │ PDFs               │
 │ SQL/CSV Data       │
 │ JSON Logs          │
 │ Audit Records      │
 └────────────────────┘
    ↓
Context Ranking
    ↓
Confidence Scoring
    ↓
Grounded Response Generation
    ↓
Citations + Traceability
    ↓
Final Secure Enterprise Response
```

---

# 🔥 Key Innovation

> RBAC authorization is enforced BEFORE vector retrieval and BEFORE response generation to guarantee zero unauthorized context exposure.

---

# 🧪 Example Enterprise Query

```json
{
  "query": "Show failed login attempts in finance systems",
  "user_role": "finance"
}
```

---

# 📡 API Endpoints

| Method | Endpoint       | Description               |
| ------ | -------------- | ------------------------- |
| POST   | `/query`       | Main enterprise RAG query |
| GET    | `/health`      | System health check       |
| GET    | `/rbac/check`  | RBAC validation           |
| GET    | `/system/info` | System capabilities       |
| GET    | `/docs`        | Swagger API documentation |

---

# 🛠️ Tech Stack

## Backend

* FastAPI
* Python
* LangChain

## AI / Retrieval

* SentenceTransformers
* FAISS
* BM25
* Hybrid Search

## Frontend

* Streamlit

## Security

* RBAC
* JWT-ready architecture

## Data Processing

* Pandas
* PyPDF
* SQLAlchemy

---

# 📂 Project Structure

```text
IntelliRAG-X/
│
├── backend/
│   ├── app.py
│   ├── rag_engine.py
│   ├── rbac.py
│   ├── ingest.py
│   └── data/
│
├── frontend/
│   └── app.py
│
├── docs/
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/IntelliRAG-X.git
cd IntelliRAG-X
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Backend

```bash
python app.py
```

## Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

# 🌐 Access Application

## Backend API

```text
http://127.0.0.1:8000/docs
```
<img width="899" height="395" alt="image" src="https://github.com/user-attachments/assets/0a5721cd-d18e-4a2b-92a5-748b90dae72e" />



## Frontend Dashboard


<img width="959" height="407" alt="image" src="https://github.com/user-attachments/assets/443c8747-f9c6-4e8e-89b7-1ef6a2f3b860" />

```text
http://localhost:8501
```

---

# 📈 Enterprise Capabilities

✅ Hybrid semantic retrieval
✅ Multi-source enterprise ingestion
✅ RBAC-aware secure retrieval
✅ Citation-backed explainability
✅ Confidence indicators
✅ Retrieval traceability
✅ Hallucination minimization
✅ Enterprise deployment architecture

---

# 🎯 Target Enterprise Use Cases

* Banking & Finance
* Healthcare
* Insurance
* Manufacturing
* Enterprise Operations
* Compliance Monitoring
* Security Intelligence
* Internal Knowledge Systems

---

# 📸 Screenshots

## Enterprise Dashboard

(Add Streamlit UI screenshot here)

## Swagger API Docs

(Add FastAPI docs screenshot here)

---

# 🔮 Future Enhancements

* GraphRAG integration
* Agentic workflows
* Multi-agent orchestration
* Real-time ingestion
* Cloud-native deployment
* AI workflow automation

---

# 👨‍💻 Developed For

SimplifyX Hiring Challenge 2026

Production-oriented Secure Enterprise AI Platform Demonstration
