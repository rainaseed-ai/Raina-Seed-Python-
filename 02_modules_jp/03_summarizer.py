import openai

def generate_summary(conversation):
    text = "\n".join([f"{c['role']}: {c['content']}" for c in conversation])
    prompt = f"以下の会話を短く要約してください:\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
