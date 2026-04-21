<<<<<<< HEAD
# AutoStream AI Agent

## Overview
This project implements a conversational AI agent that converts user interactions into qualified leads.

## Features
- Intent Detection (Greeting, Inquiry, High-Intent)
- RAG-based Knowledge Retrieval
- Lead Capture Tool Execution
- Stateful Conversation Memory

## Tech Stack
- Python
- LangChain
- FAISS
- OpenAI
- Streamlit

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Add OpenAI API key in `.env`

3. Run:
   streamlit run app.py

## Architecture
The system uses a modular architecture:
- RAG pipeline retrieves relevant knowledge from a local document using embeddings and FAISS.
- Intent detection routes user queries into different flows.
- Stateful memory ensures multi-turn conversation handling.
- Tool execution is triggered only after collecting required lead information.

## WhatsApp Integration
This agent can be integrated using WhatsApp Business API:
- Use a webhook (Flask/FastAPI) to receive messages
- Pass messages to agent logic
- Send responses back via API
=======
# autostream-ai-assistant
AutoStream AI Assistant built with Streamlit and LangChain. Detects user intent, answers queries using a local knowledge base (RAG), and captures leads through a multi-step conversational flow.
>>>>>>> 352805969ccd7ffdd20fe952d53560174c7be013
