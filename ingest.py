"""Data Ingestion Engine for Multi-Format Enterprise Data"""
import os
import json
from typing import List, Dict
from pathlib import Path

class DataIngestionEngine:
    """Handles PDF, CSV, JSON, SQL data ingestion"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.documents = []
    
    def ingest_json_logs(self, file_path: str) -> List[Dict]:
        """Ingest JSON log files"""
        documents = []
        try:
            with open(file_path, 'r') as f:
                logs = json.load(f)
                if isinstance(logs, list):
                    for log in logs:
                        documents.append({
                            "content": json.dumps(log),
                            "source": file_path,
                            "department": log.get("department", "operations"),
                            "type": "log",
                            "metadata": log
                        })
        except Exception as e:
            print(f"Error ingesting {file_path}: {e}")
        return documents
    
    def ingest_json_policies(self, file_path: str) -> List[Dict]:
        """Ingest JSON policy files"""
        documents = []
        try:
            with open(file_path, 'r') as f:
                policies = json.load(f)
                documents.append({
                    "content": json.dumps(policies, indent=2),
                    "source": file_path,
                    "department": "operations",
                    "type": "policy",
                    "metadata": policies
                })
        except Exception as e:
            print(f"Error ingesting {file_path}: {e}")
        return documents
    
    def ingest_all_data(self, data_dir: str = None) -> List[Dict]:
        """Ingest all data from data directory"""
        if data_dir is None:
            data_dir = self.data_dir
            
        all_documents = []
        data_path = Path(data_dir)
        
        if not data_path.exists():
            print(f"Data directory not found: {data_dir}")
            return all_documents
        
        # Ingest logs
        logs_dir = data_path / "logs"
        if logs_dir.exists():
            for log_file in logs_dir.glob("*.json"):
                all_documents.extend(self.ingest_json_logs(str(log_file)))
        
        # Ingest policies
        policies_dir = data_path / "policies"
        if policies_dir.exists():
            for policy_file in policies_dir.glob("*.json"):
                all_documents.extend(self.ingest_json_policies(str(policy_file)))
        
        self.documents = all_documents
        return all_documents
    
    def get_documents(self) -> List[Dict]:
        """Get all ingested documents"""
        return self.documents
