import streamlit as st
from rag_engine import get_gemini_chat, send_message

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("""
<h1 style="display:flex; align-items:center; gap:10px;">
    <img src="https://cdn.dribbble.com/userupload/44096338/file/original-d9f23e7b789ee4786429e2f3da24d01b.gif" width="60">
    Electrix AI
</h1>
""", unsafe_allow_html=True)
    st.markdown("Powered by **Ollama (Local LLM)**")
with col2:
    st.markdown("""
    <div style='text-align: right; padding: 20px 0;'>
    <small>💡 Ask anything!</small>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    # Show which model is being used
    if "model_info" in st.session_state:
        st.success(f"✓ Using: {st.session_state.model_info}")
    else:
        st.info("✓ Model initializing...")

    # Control buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🗑️ Clear", use_container_width=True, help="Clear chat history"):
            st.session_state.messages = []
            st.session_state.stop_generation = False
            st.rerun()

    with col2:
        if st.session_state.get("generating", False):
            if st.button("⏹️ Stop", use_container_width=True, key="stop_btn", help="Stop response generation"):
                st.session_state.stop_generation = True
                st.session_state.generating = False
                st.info("⏹️ Response generation stopped")
                st.rerun()

    st.divider()
    st.markdown("""
    ### About This App
    - **Type**: Direct AI Chat
    - **Model**: Ollama (Local)
    - **Memory**: Maintains chat history
    - **Privacy**: Works offline ✓

    ### Setup Info
    1. Install: https://ollama.ai
    2. Run: `ollama serve`
    3. Pull: `ollama pull mistral`
    4. Ready! ✓
    """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize chain
if "chain" not in st.session_state:
    with st.spinner("🔄 Initializing AI..."):
        try:
            chain, model_info = get_gemini_chat()
            st.session_state.chain = chain
            st.session_state.model_info = model_info
            st.session_state.initialized = True
        except Exception as e:
            st.error(f"❌ Error initializing AI: {e}")
            st.session_state.initialized = False

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize generation state
if "generating" not in st.session_state:
    st.session_state.generating = False
if "stop_generation" not in st.session_state:
    st.session_state.stop_generation = False

# Chat input
if "chain" in st.session_state and st.session_state.get("initialized", False):
    if prompt := st.chat_input("Type your question here... 💬"):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.generating = True
        st.session_state.stop_generation = False

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI response
        with st.chat_message("assistant"):
            placeholder = st.empty()

            # Check if stop was requested
            if st.session_state.stop_generation:
                placeholder.warning("⏹️ Response generation was stopped by user")
                answer = "⏹️ Response generation was stopped"
                st.session_state.messages.append({"role": "assistant", "content": answer})
                st.session_state.generating = False
            else:
                with st.spinner("⚡ Getting response..."):
                    try:
                        # Get response
                        response = send_message(
                            st.session_state.chain,
                            prompt
                        )

                        if response["success"]:
                            answer = response["answer"]
                            placeholder.markdown(answer)
                        else:
                            error_msg = f"❌ Error: {response.get('error', 'Unknown error')}"
                            placeholder.error(error_msg)
                            answer = error_msg

                        # Add assistant response to history
                        st.session_state.messages.append({"role": "assistant", "content": answer})

                    except Exception as e:
                        error_msg = f"❌ Error: {str(e)[:100]}"
                        placeholder.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
                    finally:
                        st.session_state.generating = False
                        st.session_state.stop_generation = False
else:
    if not st.session_state.get("initialized", False):
        st.warning("⚠️ AI is initializing... Please wait or refresh the page.")
