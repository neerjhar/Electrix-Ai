# ECE AI Assistant - Complete Setup & Implementation Guide

## Overview

The **Engineering AI Assistant** is a **Retrieval-Augmented Generation (RAG) application** that combines:
- **Document Intelligence**: PDF parsing and semantic understanding
- **Vector Search**: Fast similarity search across documents
- **AI Generation**: Google Gemini 1.5 Pro for intelligent responses
- **Web Interface**: Streamlit for user-friendly interaction

---

## Part 1: Project Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                  User Interface (Streamlit)                 │
│           - Chat interface                                  │
│           - Document upload (data/ folder)                 │
│           - Response display with sources                   │
└─────────────┬───────────────────────────────────────────────┘
              │ User Query
              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Embedding Pipeline                        │
│  - SentenceTransformer (all-MiniLM-L6-v2)                  │
│  - Converts text to 384-dimensional vectors                │
└─────────────┬───────────────────────────────────────────────┘
              │ Query Vector
              ▼
┌─────────────────────────────────────────────────────────────┐
│              Vector Database (ChromaDB)                      │
│  - Stores document embeddings                              │
│  - Semantic search (cosine similarity)                     │
│  - Persistent storage (chroma_db/)                         │
└─────────────┬───────────────────────────────────────────────┘
              │ Top 3 Relevant Docs
              ▼
┌─────────────────────────────────────────────────────────────┐
│           LLM Processing (Google Gemini 1.5 Pro)            │
│  - Temperature: 0.2 (consistent, focused responses)        │
│  - Context: User query + retrieved documents               │
│  - Generates answer based on available context             │
└─────────────┬───────────────────────────────────────────────┘
              │ Generated Response
              ▼
┌─────────────────────────────────────────────────────────────┐
│              Response with Citations                        │
│  - Answer text                                             │
│  - Source documents referenced                            │
│  - Added to conversation history                          │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **PDF Processing** (First run)
   - PDFs loaded from `data/` folder
   - Split into 1000-char chunks (200-char overlap)
   - Converted to embeddings via SentenceTransformer
   - Stored in ChromaDB

2. **Query Processing** (Every user query)
   - User question embedded
   - Similarity search in ChromaDB
   - Top 3 documents retrieved
   - Context formatted for LLM

3. **Response Generation**
   - LLM receives: system prompt + context + user query
   - Generates answer using only provided context
   - Sources extracted and displayed

---

## Part 2: Installation & Setup

### Prerequisites
- Python 3.8 or higher
- 2GB+ free disk space (for models and embeddings)
- Internet connection (for API calls)

### Step 1: Installation

```bash
# Navigate to project directory
cd /Users/neerjhar/Desktop/python/ece-ai-assistant

# Install all dependencies
pip install -r requirements.txt
```

**What gets installed:**
- streamlit (v≥1.32.0) - Web UI
- langchain (v≥0.1.13) - LLM orchestration
- langchain-google-genai - Google API integration
- chromadb (v≥0.4.24) - Vector database
- sentence-transformers - Embedding model
- pypdf - PDF parsing
- python-dotenv - Configuration management

### Step 2: Google API Configuration

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable **Generative Language API**
4. Create an **API Key** (Credentials → API Key)
5. Edit `.env` file:
   ```
   GOOGLE_API_KEY="your_generated_api_key_here"
   ```

### Step 3: Prepare Documents

```bash
# Create data directory (if not exists)
mkdir -p data/

# Copy your PDFs
cp /path/to/your/documents/*.pdf data/
```

### Step 4: Run the Application

```bash
# Method 1: Using provided script
python3 run.py

# Method 2: Direct streamlit
cd src/
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## Part 3: Code Structure & Implementation

### File Organization

```
src/
├── __init__.py          # Package initialization (empty)
├── app.py              # Streamlit UI application
└── rag_engine.py       # RAG processing engine
```

### rag_engine.py - Core Logic

**Key Functions:**

```python
def get_vector_store():
    """
    Creates or loads ChromaDB vector store.

    On first run:
    - Loads PDFs from data/ folder
    - Splits documents into chunks (1000 chars, 200 overlap)
    - Generates embeddings using SentenceTransformer
    - Stores in ChromaDB (chroma_db/)

    On subsequent runs:
    - Loads cached embeddings (fast)
    """

def get_engineering_chain():
    """
    Creates the complete RAG chain.

    Components:
    1. LLM: ChatGoogleGenerativeAI (Gemini 1.5 Pro)
    2. Retriever: Vector store with k=3 (top 3 docs)
    3. Prompt: System template for engineer assistant
    4. Chain: Retrieval + QA combination

    Returns: Chain ready to invoke with {"input": query}
    """
```

**Configuration Parameters:**

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Model Name (Embeddings) | all-MiniLM-L6-v2 | 384-dim embeddings, fast, accurate |
| Chunk Size | 1000 | Characters per document chunk |
| Chunk Overlap | 200 | Preserves context at boundaries |
| LLM Temperature | 0.2 | Low randomness for factual answers |
| Retrieval K | 3 | Number of documents to retrieve |
| LLM Model | gemini-1.5-pro | Google's latest multimodal LLM |

### app.py - Streamlit Interface

**Features:**

```python
# Page Configuration
st.set_page_config(...)  # Title, icon, layout

# Session State Management
st.session_state.chain       # RAG chain (initialized once)
st.session_state.messages    # Chat history

# Chat Interface
st.chat_message()    # Display user/assistant messages
st.chat_input()      # User input field
st.spinner()         # Loading indicator
st.expander()        # Collapsible source documents

# Data Flow
User Input → Query RAG Chain → Display Response → Store in History
```

---

## Part 4: Technologies & Dependencies

### Core Libraries

1. **Streamlit**
   - Purpose: Web framework for data apps
   - Usage: UI components, session state, chat interface
   - Cost: Free, open-source

2. **LangChain**
   - Purpose: Framework for LLM applications
   - Usage: Chain orchestration, prompt management
   - Components: Chains, retrievers, memory

3. **Google Generative AI**
   - Purpose: LLM API access
   - Model: Gemini 1.5 Pro
   - Cost: Free tier available, pay-as-you-go after

4. **ChromaDB**
   - Purpose: Vector database
   - Usage: Store and search document embeddings
   - Persistence: File-based storage (chroma_db/)

5. **Sentence Transformers**
   - Purpose: Embedding model
   - Model: all-MiniLM-L6-v2
   - Size: ~86MB, runs locally (no API calls)

6. **PyPDF**
   - Purpose: PDF parsing
   - Usage: Extract text from PDF documents

### Dependency Chain

```
streamlit
    ├── altair (plotting)
    ├── pandas (data handling)
    └── ... (various utilities)

langchain
    ├── pydantic (validation)
    ├── requests (HTTP)
    └── ... (utilities)

langchain-google-genai
    └── google-generativeai

chromadb
    ├── hnswlib (similarity search)
    └── sqlite3 (metadata)

sentence-transformers
    ├── torch (neural network)
    ├── transformers (NLP models)
    └── scikit-learn (similarity)

pypdf
    └── (PDF extraction)
```

---

## Part 5: Troubleshooting

### Common Issues & Solutions

#### 1. Import Errors
```
Error: ModuleNotFoundError: No module named 'streamlit'
Solution: pip install -r requirements.txt
```

#### 2. API Key Issues
```
Error: Invalid API key or authentication failed
Solution:
- Verify .env file has GOOGLE_API_KEY="your_key"
- Check key is valid at https://console.cloud.google.com/
- Ensure no extra quotes or spaces
```

#### 3. No PDFs Found
```
Error: No documents to process
Solution:
- Create data/ folder: mkdir -p data/
- Add PDF files to data/ folder
- Restart application
```

#### 4. Slow First Run
```
Issue: Application taking long time to start
Reason: Creating embeddings for all documents (normal)
Solution: Wait for completion, subsequent runs are fast
```

#### 5. Port Already in Use
```
Error: Port 8501 already in use
Solution:
streamlit run app.py --server.port 8502
```

---

## Part 6: Performance Optimization

### Speed Tips

1. **PDF Preprocessing**
   - Use search-friendly PDFs (not scanned images)
   - Smaller file sizes = faster processing
   - Break large documents into chapters

2. **Embedding Model**
   - all-MiniLM-L6-v2 is fast and accurate
   - GPU acceleration available if you have CUDA
   - Install: pip install torch torchvision torchaudio

3. **Vector DB Caching**
   - First run: ~1 min per 100 pages (depends on size)
   - Subsequent runs: <1 second (cached)
   - Clear cache: rm -rf chroma_db/

4. **LLM Optimization**
   - Temperature 0.2 = faster, more consistent
   - Lower token count = faster responses
   - Gemini 1.5 Pro = balanced speed/quality

---

## Part 7: Advanced Configuration

### Customization Options

#### Change Embedding Model
```python
# In rag_engine.py
embeddings = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"  # Try: sentence-t5-base, all-mpnet-base-v2
)
```

#### Adjust Chunk Size
```python
# Larger chunks = broader context, fewer results
# Smaller chunks = precise answers, more results
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Characters
    chunk_overlap=200       # Overlap for context
)
```

#### Change LLM Temperature
```python
# Lower (0.0) = focused, consistent
# Higher (1.0) = creative, varied
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.2  # Try: 0.0-1.0
)
```

#### Retrieve Different Number of Documents
```python
# More docs = more context, slower
# Fewer docs = faster, tighter focus
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}  # Try: 1-5
)
```

---

## Part 8: Project Files Reference

### requirements.txt
All dependencies with versions for reproducibility

### .env
Configuration file with API keys (never commit with real keys!)

### run.py
Entry point script that sets up working directory and runs Streamlit

### .gitignore
Prevents committing sensitive files (.env, __pycache__, etc.)

### README.md
User-facing documentation

### SETUP_GUIDE.md (this file)
Technical implementation guide

---

## Part 9: Deployment Considerations

### Local Development
✓ Perfect for:
- Testing and development
- Small datasets (<1GB)
- Personal use
- Private documents

### Production Deployment
Consider:
- Streamlit Cloud: https://streamlit.io/cloud
- Docker containerization
- API-based backend
- Database optimization
- Scaling for multiple users

---

## Summary

| Aspect | Details |
|--------|---------|
| **Purpose** | Engineering Q&A with document context |
| **Tech Stack** | Python, Streamlit, LangChain, ChromaDB, Gemini |
| **Architecture** | RAG (Retrieval-Augmented Generation) |
| **Speed** | Fast (~1-2 sec per query after setup) |
| **Accuracy** | High (context-aware, source-citing) |
| **Cost** | Free-tier Google API, free open-source tools |
| **Setup Time** | ~10 minutes (including API key) |

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Configure Google API key
3. ✅ Add PDF documents
4. ✅ Run: `python3 run.py`
5. ✅ Ask questions!

---

*This guide provides a complete understanding of the ECE AI Assistant project's architecture, implementation, and usage.*
