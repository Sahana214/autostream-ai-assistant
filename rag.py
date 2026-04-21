def retrieve_answer(query):
    query = query.lower()

    if "basic" in query:
        return """Basic Plan:
- $29/month
- 10 videos/month
- 720p resolution"""

    elif "pro" in query:
        return """Pro Plan:
- $79/month
- Unlimited videos
- 4K resolution
- AI captions"""

    elif "price" in query or "plan" in query:
        return """AutoStream Plans:

Basic Plan:
- $29/month
- 10 videos/month
- 720p resolution

Pro Plan:
- $79/month
- Unlimited videos
- 4K resolution
- AI captions"""

    elif "refund" in query:
        return "No refunds after 7 days"

    elif "support" in query:
        return "24/7 support is available only on the Pro plan"

    return "I can help with pricing, plans, and features of AutoStream."