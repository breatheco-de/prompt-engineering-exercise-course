import os
from groq import Groq
# Load the API key from the .env file
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def create_prompt(system_message, user_message):
    messages = [
        {
            "role": "system",
            "content": system_message,
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]

    chat_completion=  client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
        max_tokens=4095,
    )
    return chat_completion.choices[0].message.content
