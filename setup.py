#!/usr/bin/env python3
"""Setup script for IntelliRAG-X project"""
import os
import sys

def setup_directories():
    """Create project directory structure"""
    base_path = r'd:\simpilify X\IntelliRAG-X'
    
    directories = [
        os.path.join(base_path, 'backend', 'data', 'logs'),
        os.path.join(base_path, 'backend', 'data', 'policies'),
        os.path.join(base_path, 'backend', 'data', 'pdfs'),
        os.path.join(base_path, 'frontend'),
        os.path.join(base_path, 'docs'),
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created: {directory}")
    
    return base_path

if __name__ == '__main__':
    try:
        base = setup_directories()
        print(f"\n🎉 Project structure ready at: {base}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
