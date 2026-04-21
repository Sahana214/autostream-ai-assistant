<<<<<<< HEAD
<<<<<<< HEAD
# AutoStream AI Agent
=======
# AutoStream AI Assistant
>>>>>>> 69dd36ca44230ff14e7c6e098dd75dc94eea2090

## Overview
This project implements a conversational AI assistant that interacts with users, answers queries about AutoStream plans, and converts high-intent users into qualified leads.

## Features
- Intent Detection (Greeting, Inquiry, High-Intent)
- Retrieval-based responses using a local knowledge base (RAG)
- Multi-step Lead Capture Flow (Name, Email, Platform)
- Stateful Conversation Handling using LangChain Memory
- Tool Execution for storing lead information
- Interactive chat UI using Streamlit

## Tech Stack
- Python
- Streamlit
- LangChain (ConversationBufferMemory)

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   streamlit run app.py

## Architecture
The system follows a modular agent-based design:
- Intent detection routes user queries into appropriate flows
- A local knowledge base is used for retrieval-based responses (RAG)
- LangChain memory manages multi-turn conversations
- Lead capture is triggered after collecting required user details

<<<<<<< HEAD
## WhatsApp Integration
This agent can be integrated using WhatsApp Business API:
- Use a webhook (Flask/FastAPI) to receive messages
- Pass messages to agent logic
- Send responses back via API
=======
# autostream-ai-assistant
AutoStream AI Assistant built with Streamlit and LangChain. Detects user intent, answers queries using a local knowledge base (RAG), and captures leads through a multi-step conversational flow.
>>>>>>> 352805969ccd7ffdd20fe952d53560174c7be013
=======
## WhatsApp Integration (Future Scope)
This agent can be integrated with WhatsApp Business API using a webhook-based backend (Flask/FastAPI). Incoming messages can be processed through the agent logic, and responses can be sent back via API.
>>>>>>> 69dd36ca44230ff14e7c6e098dd75dc94eea2090
