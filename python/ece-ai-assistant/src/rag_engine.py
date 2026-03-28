import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
import hashlib

load_dotenv()

# Simple cache for responses
_response_cache = {}

# Configuration - choose your model here!
USE_OLLAMA = os.getenv("USE_OLLAMA", "false").lower() == "true"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")  # or "llama2", "neural-chat", etc.
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def get_gemini_chat():
    """
    Create a pure AI chat interface - supports both Google Gemini and Ollama.
    Direct AI responses using your chosen model.
    Returns: (chain, model_info)
    """

    if USE_OLLAMA:
        print(f"🦙 Using Ollama ({OLLAMA_MODEL}) at {OLLAMA_BASE_URL}")
        llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0.5,
            top_p=0.8,
            num_predict=1024
        )
        model_info = f"Ollama - {OLLAMA_MODEL}"
    else:
        print("🔵 Using Google Gemini Pro")
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.5,
            max_output_tokens=1024,
            top_p=0.8,
            timeout=30
        )
        model_info = "Google Gemini Pro"

    system_prompt = (
        "You are an expert engineering assistant and knowledgeable AI. "
        "Answer questions clearly and comprehensively. "
        "Provide helpful explanations with examples when relevant. "
        "Use mathematical formulas and code where appropriate. "
        "Be conversational and helpful."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    chain = prompt | llm

    # Return chain and model info separately (can't add attributes to chain)
    return chain, model_info


def send_message(chain, user_message, chat_history=None):
    """
    Send a message to Gemini and get a response with caching for speed.

    Args:
        chain: The Gemini chat chain
        user_message: User's input text
        chat_history: List of previous messages (optional)

    Returns:
        Dictionary with response and metadata
    """
    try:
        # Create cache key from message
        cache_key = hashlib.md5(user_message.lower().encode()).hexdigest()

        # Check cache first (FAST!)
        if cache_key in _response_cache:
            return {
                "answer": _response_cache[cache_key],
                "success": True,
                "cached": True
            }

        # Get response from API
        response = chain.invoke({"input": user_message})
        answer = response.content if hasattr(response, 'content') else str(response)

        # Store in cache
        _response_cache[cache_key] = answer

        return {
            "answer": answer,
            "success": True,
            "cached": False
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}",
            "success": False,
            "error": str(e)
        }
