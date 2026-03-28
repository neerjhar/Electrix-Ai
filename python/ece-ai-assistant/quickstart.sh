#!/bin/bash
# Quick Start Script for ECE AI Assistant

echo "=================================================="
echo "  ECE AI Assistant - Quick Start Setup"
echo "=================================================="
echo ""

# Check Python
echo "🐍 Checking Python installation..."
python3 --version || { echo "❌ Python 3 not found!"; exit 1; }
echo "✓ Python is installed"
echo ""

# Check if dependencies are installed
echo "📦 Checking dependencies..."
python3 -c "import streamlit" 2>/dev/null && echo "✓ Streamlit installed" || echo "⚠ Streamlit not installed"
python3 -c "import langchain" 2>/dev/null && echo "✓ LangChain installed" || echo "⚠ LangChain not installed"
python3 -c "import chromadb" 2>/dev/null && echo "✓ ChromaDB installed" || echo "⚠ ChromaDB not installed"
echo ""

# Ask to install dependencies if missing
read -p "Install dependencies? (y/n) " choice
if [[ "$choice" == "y" ]] || [[ "$choice" == "Y" ]]; then
    echo "📥 Installing dependencies from requirements.txt..."
    python3 -m pip install -r requirements.txt
    echo "✓ Dependencies installed"
    echo ""
fi

# Check directories
echo "📁 Checking project structure..."
mkdir -p data
mkdir -p chroma_db
echo "✓ Directories ready"
echo ""

# Check .env file
echo "🔑 Checking configuration..."
if grep -q "your_actual_api_key_here" .env; then
    echo "⚠ GOOGLE_API_KEY not set in .env file"
    echo ""
    echo "To set up your API key:"
    echo "1. Visit: https://console.cloud.google.com/"
    echo "2. Create a project and enable Generative Language API"
    echo "3. Generate an API key"
    echo "4. Edit .env file and replace 'your_actual_api_key_here'"
    echo ""
    read -p "Continue anyway? (y/n) " choice
    if [[ ! "$choice" == "y" ]] && [[ ! "$choice" == "Y" ]]; then
        echo "⛔ Please configure .env file first"
        exit 1
    fi
else
    echo "✓ .env configured"
fi
echo ""

# Check for PDFs
pdf_count=$(find data -name "*.pdf" 2>/dev/null | wc -l)
if [ $pdf_count -eq 0 ]; then
    echo "⚠ No PDF files found in data/ folder"
    echo "📄 Add your PDF documents to: $(pwd)/data/"
    echo ""
fi

echo "=================================================="
echo "  Ready to Launch!"
echo "=================================================="
echo ""
echo "Starting Streamlit application..."
echo "The app will open in your browser at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

python3 run.py
