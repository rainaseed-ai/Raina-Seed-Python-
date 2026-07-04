def get_ai_reply_template():
    reply = input("AIの返答（例: おっけー！）を入力してください: ").strip()
    return reply if reply else "了解しました"
