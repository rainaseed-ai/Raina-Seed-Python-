# ============================
#   Raina's Seed- Module Edition
#   Name setting + AI reply + Summary + Turn control
# ============================

import openai
from modules.name_config import get_user_name
from modules.ai_reply import get_ai_reply_template
from modules.summarizer import generate_summary
from modules.turn_control import should_summarize

# --- Initial Setup ---
USER_NAME = get_user_name()
AI_REPLY = get_ai_reply_template()

conversation = [
    {"role": "system", "content": "You are an AI assistant who supports the user."}
]

turn_count = 0

# --- Main Loop  ---
while True:
    user_message = input(f"{USER_NAME}: ")
    conversation.append({"role": "user", "content": user_message})
    turn_count += 1

    # ---  Summary Handling---
    if should_summarize(turn_count):
        summary = generate_summary(conversation)
        conversation = [
            {"role": "system", "content": f"Summary: {summary}"}
        ]
        turn_count = 0
        print("（Conversation was long, so it has been summarized.）")

    # --- AI Reply ---
    assistant_reply = AI_REPLY
    conversation.append({"role": "assistant", "content": assistant_reply})
    print(f"AI: {assistant_reply}")
