import streamlit as st
from google import genai

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 My AI Chatbot")
st.write("Ask anything and AI will respond.")

# Connect to Gemini
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate AI response
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=user_input
        )

        ai_message = response.text

        with st.chat_message("assistant"):
            st.write(ai_message)

        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_message
        })

    except Exception as e:
        st.error(f"Error generating answer: {e}")