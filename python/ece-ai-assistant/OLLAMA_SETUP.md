# 🦙 Ollama Setup Guide - Run LLM Locally

Want to use a **local LLM** instead of Google Gemini? **Ollama is perfect!**

## ✨ Why Use Ollama?

| Feature | Google Gemini | Ollama (Local) |
|---------|---------------|----------------|
| **API Key** | Required ✗ | Not needed ✓ |
| **Cost** | Free tier + quota | Free ✓ |
| **Privacy** | Cloud ✗ | Local ✓ |
| **Offline** | No ✗ | Yes ✓ |
| **Speed** | Depends on internet | Depends on CPU |
| **Memory** | Cloud | Local (3-20GB) |
| **Setup** | Simple | Few steps |

---

## 🚀 Quick Start

### 1. Install Ollama

Download from: **https://ollama.ai**

Supports:
- 🍎 macOS
- 🐧 Linux
- 🪟 Windows

### 2. Pull a Model

Open terminal and run:

```bash
# Recommended for chat (5GB, fast)
ollama pull mistral

# OR other options:
ollama pull llama2          # Good general model
ollama pull neural-chat     # Optimized for chat
ollama pull tinyllama       # Fast but less capable
```

### 3. Start Ollama Server

```bash
ollama serve
```

You should see:
```
serving on 127.0.0.1:11434
```

Leave this running! Open a new terminal for next step.

### 4. Configure Your App

Edit `.env` file:

```
USE_OLLAMA=true
OLLAMA_MODEL=mistral
OLLAMA_BASE_URL=http://localhost:11434
```

### 5. Run Your App

```bash
python3 run.py
```

**Done!** It should now use Ollama! 🦙

---

## 📊 Popular Ollama Models

### ⭐ Recommended (Balanced)

**Mistral** (Fastest, good quality)
```bash
ollama pull mistral
# Size: 5GB | Speed: Fast | Quality: Good
# Best for: Most tasks
```

**Neural Chat** (Chat optimized)
```bash
ollama pull neural-chat
# Size: 5GB | Speed: Fast | Quality: Good
# Best for: Conversation
```

### 🚀 Small & Fast

**TinyLlama** (Smallest)
```bash
ollama pull tinyllama
# Size: 600MB | Speed: Very Fast | Quality: Basic
# Best for: Quick answers, low memory
```

**Phi** (Small but capable)
```bash
ollama pull phi
# Size: 2GB | Speed: Very Fast | Quality: Good
# Best for: Budget machines
```

### 🧠 Large & Capable

**Llama 2** (General purpose)
```bash
ollama pull llama2
# Size: 5GB | Speed: Medium | Quality: Excellent
# Best for: Complex tasks
```

**Mixtral** (Very powerful)
```bash
ollama pull mixtral
# Size: 20GB+ | Speed: Slow | Quality: Excellent
# Best for: High-quality responses
```

---

## ⚙️ Configuration

### Edit `.env`:

```properties
# Use Ollama instead of Google
USE_OLLAMA=true

# Which model to use
OLLAMA_MODEL=mistral

# Where Ollama is running
OLLAMA_BASE_URL=http://localhost:11434
```

### Common Models:

```bash
mistral            # ⭐ Recommended
neural-chat        # Chat focused
llama2             # General purpose
tinyllama          # Fast & small
phi                # Small & capable
dolphin-mix        # Very capable
```

---

## 🎯 Quick Examples

### Example 1: Fast Setup (Mistral)

```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Pull model
ollama pull mistral

# Edit .env:
USE_OLLAMA=true
OLLAMA_MODEL=mistral

# Run app
python3 run.py
```

### Example 2: Budget Setup (TinyLlama)

```bash
# For low-power machines
ollama pull tinyllama

# .env:
USE_OLLAMA=true
OLLAMA_MODEL=tinyllama
```

### Example 3: Powerful Setup (Llama2)

```bash
# For better quality
ollama pull llama2

# .env:
USE_OLLAMA=true
OLLAMA_MODEL=llama2
```

---

## 📊 Performance Comparison

### Speed (Response Time)

| Model | Speed | Size | Quality |
|-------|-------|------|---------|
| tinyllama | ⚡⚡⚡ | 600MB | Good |
| phi | ⚡⚡⚡ | 2GB | Good |
| mistral | ⚡⚡ | 5GB | Excellent |
| llama2 | ⚡⚡ | 5GB | Excellent |
| mixtral | ⚡ | 20GB | Best |

### Memory Usage

| Model | Requires | Notes |
|-------|----------|-------|
| tinyllama | 2GB RAM | Works on most machines |
| phi | 4GB RAM | Light setup |
| mistral | 8GB RAM | Recommended min |
| llama2 | 8GB RAM | Same as mistral |
| mixtral | 16GB RAM | Need decent machine |

---

## 🆘 Troubleshooting

### Error: "Connection refused"
```bash
# Make sure ollama serve is running in another terminal!
# Terminal 1:
ollama serve

# Then run app in Terminal 2
python3 run.py
```

### Error: "Model not found"
```bash
# Pull the model first
ollama pull mistral

# Verify it's installed
ollama list
```

### Very Slow Responses
- Try smaller model: `tinyllama` or `phi`
- Close other apps (free up RAM)
- Check CPU usage
- Upgrade to better model if you have resources

### App doesn't use Ollama
- Check `.env` has: `USE_OLLAMA=true`
- Check model name is correct: `ollama list`
- Check URL is right: `http://localhost:11434`

---

## 🔄 Switching Between Models

### Keep Google Gemini

```
USE_OLLAMA=false
GOOGLE_API_KEY="your_key"
```

### Switch to Ollama

```
USE_OLLAMA=true
OLLAMA_MODEL=mistral
```

### Switch Models

```bash
# In .env, change:
OLLAMA_MODEL=llama2

# Restart app:
python3 run.py
```

---

## 💡 Pro Tips

### Tip 1: First-Time Setup Takes Time
First run downloads the model (1-20GB). Be patient!

### Tip 2: CPU Usage is Normal
Local LLM uses your CPU heavily. That's normal.

### Tip 3: Multiple Models
Can have multiple models with `ollama list`

### Tip 4: Switch During Session
Edit `.env` and reload to change models

### Tip 5: Run on Different Machine
```
OLLAMA_BASE_URL=http://192.168.1.100:11434
```
(Assuming Ollama runs on that IP)

---

## 📚 What Model Should I Choose?

### If you have:
- **512MB RAM** → Can't run Ollama
- **2GB RAM** → Use `tinyllama`
- **4GB RAM** → Use `phi` or `tinyllama`
- **8GB RAM** → Use `mistral` or `llama2`
- **16GB+ RAM** → Use `mixtral` for best quality

### Choose based on:
- **Speed**? → `tinyllama` or `phi`
- **Quality?** → `mistral`, `llama2`, or `mixtral`
- **Balanced?** → `mistral` (recommended)
- **Chat?** → `neural-chat` or `mistral`

---

## 🚀 Complete Setup Example

```bash
# 1. Install Ollama (from https://ollama.ai)

# 2. Start Ollama server (Terminal 1)
ollama serve

# 3. Pull model (Terminal 2)
ollama pull mistral

# 4. Edit .env
nano .env
# Change: USE_OLLAMA=true
# Change: OLLAMA_MODEL=mistral

# 5. Run app (Terminal 2 or 3)
python3 run.py

# 6. Open browser
# http://localhost:8501

# 7. Start chatting! 🦙
```

---

## ✅ Verify It Works

1. Run: `python3 run.py`
2. Look for: "🦙 Using Ollama (mistral)" in console
3. Check sidebar: Should show model name
4. Ask a question - should get local response

---

## 🎉 You're All Set!

Now you're running a **local LLM completely offline**!

**Benefits:**
- ✓ No API key needed
- ✓ Works offline
- ✓ Completely private
- ✓ Free to use
- ✓ Full control

**Trade-offs:**
- Takes more CPU
- Slower than cloud (depends on hardware)
- Need space (models are 600MB - 20GB+)

Enjoy your local AI! 🦙
