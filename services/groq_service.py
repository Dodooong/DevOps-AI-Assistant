import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def ask_groq(prompt, system_prompt):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

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