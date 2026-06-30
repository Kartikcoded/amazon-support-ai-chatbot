# 🛒 Amazon Support AI Chatbot

An AI-powered Amazon Customer Support Chatbot built using **Python**, **Streamlit**, and the **Google Gemini SDK**. The chatbot demonstrates how Prompt Engineering techniques can be applied to build a professional, context-aware conversational AI capable of handling common customer support queries.

---

## 📌 Project Overview

This chatbot simulates an Amazon Customer Support Executive and assists users with order-related issues such as:

- 📦 Order delivery delays
- 💳 Payment-related issues
- 🔄 Refund status
- ❌ Order cancellation
- 📱 Wrong product received
- 💬 General customer support queries

The chatbot maintains conversation history and generates natural, empathetic, and context-aware responses using Google's Gemini model.

---

## ✨ Features

- 🤖 AI-powered Amazon customer support chatbot
- 🧠 Powered by **Google Gemini SDK**
- 💬 Interactive chat interface built with Streamlit
- 📝 Multi-turn conversation support
- 😊 Professional and empathetic responses
- 🔐 Secure API key management using `.env`
- 🐳 Dockerized for easy deployment

---

# 🧠 Prompt Engineering Techniques Used

This project demonstrates the practical application of Prompt Engineering to improve chatbot quality and consistency.

### ✅ Persona-based Prompting

The model is assigned the role of a professional Amazon Customer Support Executive.

This ensures responses remain:

- Professional
- Friendly
- Empathetic
- Customer-focused

Example:

```text
You are a helpful and professional customer support agent working for Amazon.
```

---

### ✅ Instruction Prompting

The chatbot receives clear instructions about how it should behave.

Examples:

- Assist users with order-related issues.
- Always be polite and concise.
- Ask for the Order ID whenever required.
- Never assume missing information.
- Ensure customers feel supported.

---

### ✅ Few-shot Prompting

The system prompt contains multiple customer support examples that teach Gemini how to respond.

Example scenarios include:

- Order delayed
- Double payment
- Wrong product received
- Order cancellation
- Refund not received

Providing examples improves response consistency and style.

---

### ✅ Context Prompting

Conversation history is maintained using **Streamlit Session State**, enabling Gemini to generate context-aware responses during multi-turn conversations.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| Google Gemini SDK | Large Language Model |
| Prompt Engineering | Response Optimization |
| Python Dotenv | Environment Variable Management |
| Docker | Containerization |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
amazon-support-ai-chatbot/
│
├── chatbot.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/Kartikcoded/amazon-support-ai-chatbot.git

cd amazon-support-ai-chatbot
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Gemini API Key

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can generate a free Gemini API key from:

https://ai.google.dev/

---

# ▶️ Run the Application

```bash
streamlit run chatbot.py
```

Visit:

```
http://localhost:8501
```

---

# 🐳 Run with Docker

## Build Docker Image

```bash
docker build -t amazon-support-ai-chatbot .
```

## Run Docker Container

```bash
docker run --env-file .env -p 8501:8501 amazon-support-ai-chatbot
```

Visit:

```
http://localhost:8501
```

---

# 💬 Example Queries

- My order hasn't arrived yet.
- I received the wrong product.
- I was charged twice.
- Can I cancel my order?
- Where is my refund?
- My package is delayed.
- I want to return my item.

---

# 📖 Learning Outcomes

Through this project, I learned how to:

- Build AI-powered applications using the Google Gemini SDK
- Design effective system prompts
- Apply Persona-based Prompting
- Apply Instruction Prompting
- Apply Few-shot Prompting
- Maintain conversational context using Context Prompting
- Build interactive applications with Streamlit
- Containerize AI applications using Docker
- Manage environment variables securely
- Version and publish projects using Git & GitHub

---


# 👨‍💻 Author

**Kartik**

**AI Engineer | Python Backend Developer**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
