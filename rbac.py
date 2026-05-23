"""Role-Based Access Control (RBAC) Engine for IntelliRAG-X"""
import json
from typing import Dict, List
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    FINANCE = "finance"
    HR = "hr"
    ENGINEERING = "engineering"

class RBACEngine:
    """Enterprise RBAC Engine - Security enforced BEFORE retrieval"""
    
    def __init__(self):
        self.policies = self._get_default_policies()
    
    def _get_default_policies(self) -> Dict:
        """Default RBAC policies"""
        return {
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
    
    def is_authorized(self, user_role: str, department: str) -> bool:
        """Check if user role can access department"""
        role_policy = self.policies.get(user_role.lower(), {})
        
        if role_policy.get("can_access_all"):
            return True
        
        accessible_depts = role_policy.get("accessible_departments", [])
        return department.lower() in accessible_depts
    
    def filter_documents(self, user_role: str, documents: List[Dict]) -> List[Dict]:
        """Filter documents based on user role - BEFORE retrieval"""
        filtered = []
        for doc in documents:
            department = doc.get("department", "").lower()
            if self.is_authorized(user_role, department):
                filtered.append(doc)
        return filtered
    
    def can_perform_action(self, user_role: str, action: str) -> bool:
        """Check if user can perform sensitive operations"""
        role_policy = self.policies.get(user_role.lower(), {})
        return role_policy.get("sensitive_operations", False)
