def get_user_name():
    name = input("Enter your name: ").strip()
    return name if name else "User"  # ← Change this if you want a fixed name
