import ollama

def ask_ai(prompt):

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": "Ты голосовой ассистент Джарвис. Отвечай кратко и на русском."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
