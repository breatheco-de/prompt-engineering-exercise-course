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
        return string[1:-1]
    return string

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
        model="llama3-70b-8192",
        max_tokens=2000,
    )
    return remove_double_quotes_from_beginning_and_end(chat_completion.choices[0].message.content)




def save_report(content, directory):
    # Get the current file directory

    dirName = directory.split(os.sep)[-1]

    # Define the path to the report file
    report_path = os.path.join(directory, f'../../.learn/reports/{dirName}/report.md')
    # Ensure the directory exists
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    # Write content to the report file
    with open(report_path, 'w', encoding='utf-8') as file:
        file.write(content)


def delete_report(directory):
    # Get the current file directory
    dirName = directory.split(os.sep)[-1]

    # Define the path to the report file
    report_path = os.path.join(directory, f'../../.learn/reports/{dirName}/report.md')
    # Check if the report file exists and delete it
    if os.path.exists(report_path):
        os.remove(report_path)


def get_tester_prompt(requirements):
    TESTER_PROMPT = f"""
    You are an AI Teacher specializing in prompt engineering. You understand both Spanish and English, and you must respond in the same language as the user's prompt.

    Your task is to evaluate and provide feedback on the user's prompt based on the following requirements:
    ---
    {requirements}
    ---

    Analyze the user's prompt carefully. If it meets all requirements, respond with:

    '''
    # GOOD_PROMPT ✅
    [Provide encouraging feedback in the user's language, explaining why the prompt is effective]
    '''

    If the prompt does not meet all requirements or is too vague, respond with:
    '''
    # BAD_PROMPT 🚩 
    [Provide a concise summary of why the prompt needs improvement, in the user's language]

    | Requirement | Evaluation |
    |-------------|------------|
    [Create a table with each requirement, using ✅ for met requirements and ❌ for those not met, with brief explanations]

    [Offer specific suggestions for improving the prompt, addressing each unmet requirement]

    > [Provide an example prompt that should word inside a markdown blockquote ]
    '''

    Remember:
    1. Always respond in the same language as the user's prompt (Spanish or English).
    2. Be constructive and encouraging in your feedback.
    3. If a requirement is implicitly addressed, consider it met.
    4. Never include "GOOD_PROMPT" in a response for an inadequate prompt.
    5. Tailor your feedback to help the user understand prompt engineering principles.

    Your goal is to guide the user in creating effective prompts that will elicit the desired response from an AI system.
    """
    return TESTER_PROMPT