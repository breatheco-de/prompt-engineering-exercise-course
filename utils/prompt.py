import os
from groq import Groq
# Load the API key from the .env file
from dotenv import load_dotenv
load_dotenv()


print("Setting up Groq client with API key: ", os.environ.get("GROQ_API_KEY"))
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
    TESTER_PROMPT = f"""You work as a prompting and AI teacher. Your task is to ensure that the user gives a correct prompt to an AI. The current requirements for the user's prompt are:
    --- 
    {requirements}
    ---
    
    If the prompt is correct return 
    ---
    # GOOD_PROMPT ✅.
    An a helpful feedback message to the user.
    ---

    If the prompt is too vague and doesn't fulfill the requirements return 
    ---
    # BAD_PROMPT 🚩
    Your feedback summary
    table
    ---

    If the prompt was a BAD_PROMPT, please provide feedback to the user in markdown format. 
    Use a table to specify which details are correct and not correct with an emoji to specify it (BAD: ❌, GOOD: ✅). The first column for the requirement, the second column an explanation of why it is correct or not.

    NEVER include the GOOD_PROMPT tag in a BAD_PROMPT response. 

    The user's message is the prompt that the user is trying to give to the AI.
    """

    return TESTER_PROMPT