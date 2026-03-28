# 🤖 AI Chat Assistant

A simple, powerful **Gemini AI Chat Application** powered by Google's Generative AI API. No PDFs needed - just pure conversational AI!

## ✨ Features

✅ **Pure Gemini API** - Direct responses from Google's AI
✅ **No PDF Required** - Works like ChatGPT
✅ **Conversation Memory** - Maintains chat history
✅ **Fast & Responsive** - Instant API responses
✅ **Clean Web Interface** - Built with Streamlit
✅ **No Data Upload** - Everything stays private
✅ **Minimal Setup** - Just need an API key

## 🚀 Quick Start

### 1. Get Your Google API Key

1. Visit: https://console.cloud.google.com/
2. Create a new project
3. Search for **"Generative Language API"** and enable it
4. Go to **Credentials** → **+ Create Credentials** → **API Key**
5. Copy your API key

### 2. Configure the App

Edit `.env` file and add your API key:
```
GOOGLE_API_KEY="your_api_key_here"
```

### 3. Run the App

```bash
python3 run.py
```

The app will open at: **http://localhost:8501**

## 📋 What You Get

A modern chat interface similar to ChatGPT where you can:
- ✅ Ask any question
- ✅ Get instant AI responses
- ✅ Maintain conversation history
- ✅ Clear chat anytime
- ✅ No file uploads needed

## 🔧 Project Structure

```
src/
├── app.py              # Streamlit chat interface
└── rag_engine.py       # Gemini API wrapper
```

## ⚙️ Configuration

### Available Models
- `gemini-pro` - Default, works great for most queries
- `gemini-pro-vision` - Includes vision capabilities (if available)

### Customize in `rag_engine.py`

```python
# Change temperature for different responses
temperature=0.7  # 0.0 = focused, 1.0 = creative

# Change max tokens for response length
max_output_tokens=2048  # Increase for longer responses
```

## 🔐 Security

- ✅ API key stored in `.env` (excluded from git)
- ✅ No data uploaded to external servers (except API calls)
- ✅ All conversations are local
- ✅ `.gitignore` prevents accidental key commits

## 📦 Installation

### Requirements
- Python 3.8+
- Google API Key
- Internet connection

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install streamlit langchain langchain-google-genai python-dotenv google-generativeai
```

## 🎯 Use Cases

Perfect for:
- 💬 General conversation
- 🧠 Quick answers
- 📚 Learning & explanations
- 🔧 Technical assistance
- 📝 Writing & brainstorming
- 🎓 Homework help
- 💡 Creative ideas
- 🐛 Debugging code

## ⚠️ Limitations

- **No context persistence**: Chat history only in current session
- **API rate limits**: Depends on your Google Cloud plan
- **Model availability**: Depends on your API key permissions
- **No file upload**: Can't directly search files (paste text instead)

## 🆘 Troubleshooting

### "API Key Error"
- Verify `.env` has correct format: `GOOGLE_API_KEY="your_key"`
- Check key is valid at https://console.cloud.google.com/

### "Model not found"
- Some keys don't have access to all models
- Try using `gemini-pro` instead of `gemini-1.5-pro`

### "Rate limit exceeded"
- Wait a few seconds before next query
- Check your Google Cloud quota

### App not starting
- Ensure Streamlit is installed: `pip install streamlit`
- Check Python version: `python3 --version` (should be 3.8+)

## 📚 Dependencies

| Package | Purpose |
|---------|---------|
| streamlit | Web UI framework |
| langchain | LLM orchestration |
| langchain-google-genai | Google API integration |
| google-generativeai | Gemini models |
| python-dotenv | Configuration management |

## 🎨 Customization

### Change the System Prompt

Edit `rag_engine.py`:
```python
system_prompt = (
    "You are a helpful assistant. "
    "Add your instructions here..."
)
```

### Change UI Colors/Layout

Edit `app.py` to customize Streamlit appearance

### Modify Temperature

Lower = more focused and deterministic (0.0)
Higher = more creative and random (1.0)

## 🚀 Deployment

### Streamlit Cloud
```bash
streamlit run src/app.py --logger.level=error
```

Then deploy to: https://streamlit.io/cloud

### Docker
```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "src/app.py"]
```

## 📞 Support

For issues:
1. Check `.env` configuration
2. Verify API key is valid
3. Check internet connection
4. Review error messages carefully
5. Check Google Cloud console for quota/limits

## 📝 License

Free to use and modify.

## 🎓 What is This?

This is a **direct API wrapper** over Google's Gemini model. Unlike RAG (Retrieval-Augmented Generation), it:
- ❌ Doesn't need documents
- ❌ Doesn't search files
- ✅ Just talks to Gemini directly
- ✅ Works like ChatGPT/Gemini web interface

---

**Start chatting now:** `python3 run.py` 🚀
