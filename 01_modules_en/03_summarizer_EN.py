import openai

def generate_summary(conversation):
    text = "\n".join([f"{c['role']}: {c['content']}" for c in conversation])
    prompt = f"Please summarize the following conversation briefly:\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
