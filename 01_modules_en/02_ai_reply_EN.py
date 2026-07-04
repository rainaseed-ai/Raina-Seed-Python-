def get_ai_reply():
    reply = input("Enter AI reply (e.g., Sure!): ").strip()
    return reply if reply else "Understood."  # ← Change this to your preferred default reply
