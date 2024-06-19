import io
import sys
sys.stdout = buffer = io.StringIO()
import pytest
import os
# import app


import re
from utils.prompt import create_prompt, save_report, delete_report, get_tester_prompt


current_dir = os.path.dirname(os.path.abspath(__file__))


PROMPT_REQUIREMENTS = """The prompt MUST use delimiters for the text to translate. If the prompt uses delimiters and ask for a translation, then is correct. Any kind of delimiters can be used."""




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


@pytest.mark.it("The prompt MUST use delimiters to succesfully instruct the AI to translate the correct text.")

def test_prompt():
    PROMPT = open(path, "r").read()
    result = create_prompt(get_tester_prompt(PROMPT_REQUIREMENTS), PROMPT)
    
    if "BAD_PROMPT" in result:
        save_report(result, current_dir)
    else:
        delete_report(current_dir)

    assert "GOOD_PROMPT" in result


