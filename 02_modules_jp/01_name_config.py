def get_user_name():
    name = input("あなたの名前を入力してください: ").strip()
    return name if name else "ユーザー"
