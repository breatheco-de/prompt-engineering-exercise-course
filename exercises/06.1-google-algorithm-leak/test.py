import io
import sys
sys.stdout = buffer = io.StringIO()
import pytest
import os
# import app


import re
from utils.prompt import create_prompt


def save_report(content):
    # Get the current file directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dirName = current_dir.split(os.sep)[-1]

    # Define the path to the report file
    report_path = os.path.join(current_dir, f'../../.learn/reports/{dirName}/report.txt')
    # Ensure the directory exists
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    # Write content to the report file
    with open(report_path, 'w', encoding='utf-8') as file:
        file.write(content)


def delete_report():
    # Get the current file directory
    dirName = os.path.dirname(os.path.abspath(__file__))
    dirName = dirName.split('\\')[-1]

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the path to the report file
    report_path = os.path.join(current_dir, f'../../.learn/reports/{dirName}/report.txt')
    # Check if the report file exists and delete it
    if os.path.exists(report_path):
        os.remove(report_path)


PROMPT_REQUIREMENTS = """The prompt MUST pass the right context to the AI, a new about Google Algorithm Leak.
The prompt must instruct the AI to produce a sarcastic analysis of the current situation with the Google Algorithm.
The prompt MUST include the context inside delimiters to succesfully specify information to the AI.
"""

TESTER_PROMPT = f"""You work as a prompt and AI teacher. Your task is to ensure that the user gives a correct prompt to an AI. The current requirements for the user prompt are: {PROMPT_REQUIREMENTS} If the prompt is too vague and doesn't include the request information return # BAD_PROMPT 🚩. If the prompt is correct return # GOOD_PROMPT ✅.

If the prompt was a BAD_PROMPT, please provide feedback to the user on how to improve it in an appropiate markdown format.


NEVER include the GOOD_PROMPT tag in a 
"""


path = os.path.dirname(os.path.abspath(__file__)) + '/prompt.txt'

@pytest.mark.it('The PROMPT variable must exist')
def test_file_exists():
    try:
        # Check if the file in path exists
        with open(path, "r") as file:
            pass
    except FileNotFoundError:
        raise FileNotFoundError("The file 'prompt.txt' should exist in the root directory")

@pytest.mark.it('The value of PROMPT should be a non-empty string')
def test_prompt_value():
    try:
        # Check if the file in path exists
        with open(path, "r") as file:
            PROMPT = file.read()
        assert isinstance(PROMPT, str) and len(PROMPT) > 10
    except FileNotFoundError:
        raise FileNotFoundError("The file 'prompt.txt' should exist in the root directory")


@pytest.mark.it("The prompt MUST pass the right context to the AI, a new about Google Algorithm Leak. The prompt must instruct the AI to produce a sarcastic analysis of the current situation with the Google Algorithm. The prompt MUST include the context inside delimiters to succesfully specify information to the AI.")

def test_prompt():
    PROMPT = open(path, "r").read()
    result = create_prompt(TESTER_PROMPT, PROMPT)
    
    if "BAD_PROMPT" in result:
        save_report(result)
    else:
        delete_report()

    assert "GOOD_PROMPT" in result


