#!/usr/bin/env python3
"""
Auto-setup for IntelliRAG-X
Run this to create all necessary directories and files
"""
import os
import sys
import json

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = "IntelliRAG-X"

def create_dir_structure():
    """Create complete directory structure"""
    base = os.path.join(PROJECT_ROOT, PROJECT_NAME)
    
    paths = {
        'backend': os.path.join(base, 'backend'),
        'backend_data': os.path.join(base, 'backend', 'data'),
        'logs': os.path.join(base, 'backend', 'data', 'logs'),
        'policies': os.path.join(base, 'backend', 'data', 'policies'),
        'pdfs': os.path.join(base, 'backend', 'data', 'pdfs'),
        'frontend': os.path.join(base, 'frontend'),
        'docs': os.path.join(base, 'docs'),
    }
    
    for name, path in paths.items():
        os.makedirs(path, exist_ok=True)
    
    return paths

if __name__ == '__main__':
    try:
        paths = create_dir_structure()
        print("✅ Project structure created successfully!")
        for name, path in paths.items():
            exists = "✓" if os.path.exists(path) else "✗"
            print(f"  {exists} {name}: {path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
