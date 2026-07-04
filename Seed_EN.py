# ============================
#   Raina's Seed - Basic Edition (EN)
#   Name setting + AI reply + Summary + Turn control
# ============================

import openai

# --- Initial Setup ---
USER_NAME = input("Enter your name: ")
if USER_NAME.strip() == "":
    USER_NAME = "User"  # ← Change this if you want a fixed name

AI_REPLY = input("Enter AI reply (e.g., Sure!): ")
if AI_REPLY.strip() == "":
    AI_REPLY = "Understood."  # ← Change this to your preferred default reply

TURN_THRESHOLD = 20  # Summary interval (change this number)

# --- Conversation Log ---
conversation = [
    {"role": "system", "content": "You are an AI assistant who supports the user."}
]

turn_count = 0


# --- Summary Function ---
def generate_summary(conversation):
    text = "\n".join([f"{c['role']}: {c['content']}" for c in conversation])
    prompt = f"Summarize the following conversation briefly:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]


# --- Main Loop ---
while True:
    user_message = input(f"{USER_NAME}: ")
    conversation.append({"role": "user", "content": user_message})
    turn_count += 1

    # --- Summary Handling ---
    if turn_count >= TURN_THRESHOLD:
        summary = generate_summary(conversation)
        conversation = [
            {"role": "system", "content": f"Summary: {summary}"}
        ]
        turn_count = 0
        print("(Conversation was long, so it has been summarized.)")

    # --- AI Reply ---
    assistant_reply = AI_REPLY
    conversation.append({"role": "assistant", "content": assistant_reply})
    print(f"AI: {assistant_reply}")
