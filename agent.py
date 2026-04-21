from tools import mock_lead_capture
from rag import retrieve_answer
from langchain.memory import ConversationBufferMemory
# LangChain Memory
memory = ConversationBufferMemory()

def detect_intent(text):
    text = text.lower()
    if any(x in text for x in ["hi", "hello"]):
        return "greeting"

    elif any(x in text for x in ["price", "plan", "cost"]):
        return "inquiry"

    elif any(x in text for x in ["buy", "subscribe", "want", "pro plan"]):
        return "high_intent"

    return "unknown"


def agent_response(user_input, state):
    if state.stage == "ask_name":
        state.name = user_input
        state.stage = "ask_email"
        response = "Great! Please provide your email."

    elif state.stage == "ask_email":
        state.email = user_input
        state.stage = "ask_platform"
        response = "Which platform do you create content on? (YouTube/Instagram)"

    elif state.stage == "ask_platform":
        state.platform = user_input

        mock_lead_capture(state.name, state.email, state.platform)

        state.stage = None
        response = "🎉 Lead captured successfully! Our team will contact you."

    else:
        intent = detect_intent(user_input)

        if intent == "greeting":
            response = "Hi! 👋 How can I help you with AutoStream?"

        elif intent == "inquiry":
            response = retrieve_answer(user_input)

        elif intent == "high_intent":
            state.stage = "ask_name"
            response = "Awesome! Let's get you started 🚀\nWhat's your name?"

        else:
            response = "I can help with AutoStream pricing, plans, and features."

    memory.save_context({"input": user_input}, {"output": response})

    return response
