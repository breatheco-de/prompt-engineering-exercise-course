import io
import sys
sys.stdout = buffer = io.StringIO()
import pytest
import os
import app
import re
from utils.prompt import create_prompt

PROMPT_REQUIREMENTS = """The prompt MUST use delimiters for the text to translate. If the prompt uses delimiters and ask for a translation, then is correct. Any kind of delimiters can be used."""

TESTER_PROMPT = f"""You work as a prompt and AI teacher. Your task is to ensure that the user gives a correct prompt to an AI. The current requirements for the user prompt are: {PROMPT_REQUIREMENTS} If the prompt is too vague and doesn't follow the requirements return BAD_PROMPT. If the prompt is correct return GOOD_PROMPT."""


path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'

@pytest.mark.it('The PROMPT variable must exist')
def test_variable_exists():
    try:
        from app import PROMPT
    except ImportError:
        raise ImportError("The variable 'PROMPT' should exist in app.py")

@pytest.mark.it('The value of PROMPT should be a non-empty string')
def test_prompt_value():
    assert isinstance(app.PROMPT, str) and len(app.PROMPT) > 0


@pytest.mark.it("The prompt MUST use delimiters to succesfully instruct the AI to translate the correct text.")
def test_prompt():
    from app import PROMPT
    result = create_prompt(TESTER_PROMPT, PROMPT)


    # Save the result in a file response.txt
    with open("response.txt", "w") as f:
        f.write(result)

    assert "GOOD_PROMPT" in result
