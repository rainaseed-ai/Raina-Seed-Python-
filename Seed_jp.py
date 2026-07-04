# ============================
#   Raina's Seed- Module Edition
#   名前設定 + AI返答設定 + 要約 + ターン管理
# ============================

import openai
from modules.name_config import get_user_name
from modules.ai_reply import get_ai_reply_template
from modules.summarizer import generate_summary
from modules.turn_control import should_summarize

# --- 初期設定 ---
USER_NAME = get_user_name()
AI_REPLY = get_ai_reply_template()

conversation = [
    {"role": "system", "content": "あなたはユーザーに寄り添うAIです。"}
]

turn_count = 0

# --- メインループ ---
while True:
    user_message = input(f"{USER_NAME}: ")
    conversation.append({"role": "user", "content": user_message})
    turn_count += 1

    # --- 要約処理 ---
    if should_summarize(turn_count):
        summary = generate_summary(conversation)
        conversation = [
            {"role": "system", "content": f"要約: {summary}"}
        ]
        turn_count = 0
        print("（会話が長くなったため、要約して軽量化しました）")

    # --- AIの返答 ---
    assistant_reply = AI_REPLY
    conversation.append({"role": "assistant", "content": assistant_reply})
    print(f"AI: {assistant_reply}")
