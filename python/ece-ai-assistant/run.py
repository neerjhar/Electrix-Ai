#!/usr/bin/env python3
"""
Entry point for the Engineering AI Assistant Streamlit app.
This script runs the Streamlit application from the correct directory.
"""
import subprocess
import sys
import os

if __name__ == "__main__":
    # Change to src directory
    src_path = os.path.join(os.path.dirname(__file__), "src")
    os.chdir(src_path)

    # Run streamlit app
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
