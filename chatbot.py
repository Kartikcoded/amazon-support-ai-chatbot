import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit Page Config
st.set_page_config(page_title="Amazon Support Chatbot", page_icon="🛒")

st.title("🛒 Amazon Support Chatbot")

# System Prompt
SYSTEM_PROMPT = """
You are a helpful and professional customer support agent working for Amazon.

Your job is to assist users with their order and transaction-related issues in a polite, professional, and concise manner.

Rules:
- Be empathetic and courteous.
- Ask for the Order ID whenever necessary.
- Never make up order information.
- If you don't know something, politely ask for more details.
- Keep responses short and conversational.

Example 1:
User: My order hasn't arrived yet.
Assistant: I'm sorry to hear that your order hasn't arrived. Could you please share your Order ID so I can help check its delivery status?

Example 2:
User: I was charged twice.
Assistant: I apologize for the inconvenience. Please provide your Order ID along with the last four digits of the payment method used so I can assist you further.

Example 3:
User: I received the wrong item.
Assistant: I'm sorry about the mix-up. Please share your Order ID and upload a photo of the item you received. I'll help you arrange a replacement or refund.

Example 4:
User: Can I cancel my order?
Assistant: Certainly! Please provide your Order ID. If the order hasn't been shipped yet, I'll help you with the cancellation.

Example 5:
User: I haven't received my refund.
Assistant: I understand your concern. Please provide your Order ID or return tracking number so I can check the refund status for you.
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask your query...")

if user_input:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build conversation history
    conversation = SYSTEM_PROMPT + "\n\n"

    for message in st.session_state.messages:
        if message["role"] == "user":
            conversation += f"User: {message['content']}\n"
        else:
            conversation += f"Assistant: {message['content']}\n"

    # Generate response
    with st.spinner("Thinking..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        assistant_reply = response.text

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)