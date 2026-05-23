#!/usr/bin/env python3
"""Complete setup and initialization script for IntelliRAG-X"""
import os
import json
import sys
from pathlib import Path

def setup_project():
    """Setup complete IntelliRAG-X project structure and sample data"""
    
    # Create directory structure
    base_dir = Path(__file__).parent
    data_dirs = [
        base_dir / "data" / "logs",
        base_dir / "data" / "policies",
        base_dir / "data" / "pdfs",
    ]
    
    print("📁 Creating directories...")
    for d in data_dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"   ✅ {d}")
    
    # Create sample RBAC policy
    rbac_policy = {
        "admin": {
            "accessible_departments": ["finance", "hr", "engineering", "operations"],
            "can_access_all": True,
            "sensitive_operations": True
        },
        "finance": {
            "accessible_departments": ["finance"],
            "can_access_all": False,
            "sensitive_operations": False
        },
        "hr": {
            "accessible_departments": ["hr"],
            "can_access_all": False,
            "sensitive_operations": False
        },
        "engineering": {
            "accessible_departments": ["engineering"],
            "can_access_all": False,
            "sensitive_operations": False
        }
    }
    
    policy_file = base_dir / "data" / "policies" / "rbac.json"
    with open(policy_file, 'w') as f:
        json.dump(rbac_policy, f, indent=2)
    print(f"✅ Created: {policy_file}")
    
    # Create sample security logs
    security_logs = [
        {
            "timestamp": "2026-03-12T14:32:10Z",
            "department": "finance",
            "event": "Failed Login Attempt",
            "user_id": "user_5432",
            "system": "Finance-Payroll-API",
            "severity": "High",
            "details": "Multiple failed authentication attempts detected"
        },
        {
            "timestamp": "2026-03-12T15:45:22Z",
            "department": "finance",
            "event": "Unauthorized Access",
            "user_id": "user_7821",
            "system": "Financial-Reports-DB",
            "severity": "Critical",
            "details": "Attempt to access Q4 financial reports without authorization"
        },
        {
            "timestamp": "2026-03-12T16:12:08Z",
            "department": "engineering",
            "event": "Successful Login",
            "user_id": "user_1234",
            "system": "Code-Repository",
            "severity": "Low",
            "details": "Authorized login from approved IP address"
        },
        {
            "timestamp": "2026-03-13T09:15:33Z",
            "department": "hr",
            "event": "Data Export",
            "user_id": "user_4567",
            "system": "HRIS-System",
            "severity": "Medium",
            "details": "Employee records exported for payroll processing"
        }
    ]
    
    logs_file = base_dir / "data" / "logs" / "security_logs.json"
    with open(logs_file, 'w') as f:
        json.dump(security_logs, f, indent=2)
    print(f"✅ Created: {logs_file}")
    
    # Create sample audit logs
    audit_logs = [
        {
            "timestamp": "2026-03-14T08:00:00Z",
            "department": "finance",
            "event": "Revenue Report Generated",
            "user_id": "user_2341",
            "system": "Financial-Analytics",
            "severity": "Medium",
            "data_volume": "2.5 GB",
            "details": "Q4 revenue analysis generated and distributed"
        },
        {
            "timestamp": "2026-03-14T09:30:15Z",
            "department": "finance",
            "event": "Budget Allocation Review",
            "user_id": "user_3456",
            "system": "Budget-Planning-System",
            "severity": "High",
            "details": "Senior finance team reviewed budget allocation for next quarter"
        },
        {
            "timestamp": "2026-03-14T10:45:22Z",
            "department": "hr",
            "event": "Employee Onboarding",
            "user_id": "user_5678",
            "system": "HRIS-System",
            "severity": "Low",
            "details": "New employee profile created and access provisioned"
        },
        {
            "timestamp": "2026-03-14T13:20:08Z",
            "department": "engineering",
            "event": "Code Review Approval",
            "user_id": "user_7890",
            "system": "Code-Review-Platform",
            "severity": "Low",
            "details": "Critical infrastructure code approved for production deployment"
        }
    ]
    
    audit_file = base_dir / "data" / "logs" / "audit_logs.json"
    with open(audit_file, 'w') as f:
        json.dump(audit_logs, f, indent=2)
    print(f"✅ Created: {audit_file}")
    
    print("\n🎉 Project setup complete!")
    print(f"📍 Base directory: {base_dir}")
    print("\n📚 Next steps:")
    print("   1. pip install -r requirements.txt")
    print("   2. python app.py")
    print("   3. Visit http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    try:
        setup_project()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
