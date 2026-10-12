import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def ask_groq(prompt, system_prompt):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content