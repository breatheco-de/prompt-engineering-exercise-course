import os
from groq import Groq
# Load the API key from the .env file
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def remove_double_quotes_from_beginning_and_end(string):
    if string[0] == '"' and string[-1] == '"':
        print("fixing string")
        return string[1:-1]
    return string

def create_prompt(system_message, user_message):
    messages = [
        {
            "role": "system",
            "content": system_message + " Never wrap your answer inside quotes or double quotes.",
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]

    chat_completion=  client.chat.completions.create(
        messages=messages,
        model="llama3-70b-8192",
        max_tokens=2000,
    )
    return remove_double_quotes_from_beginning_and_end(chat_completion.choices[0].message.content)



