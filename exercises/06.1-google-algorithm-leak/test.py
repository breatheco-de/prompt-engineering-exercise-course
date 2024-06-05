import io
import sys
sys.stdout = buffer = io.StringIO()
import pytest
import os
import app
import re
from utils.prompt import create_prompt

PROMPT_REQUIREMENTS = """The prompt MUST pass the right context to the AI, a new about Google Algorithm Leak.
The prompt must instruct the AI to produce a sarcastic analysis of the current situation with the Google Algorithm.
The prompt MUST include the context inside delimiters to succesfully specify information to the AI.
"""

TESTER_PROMPT = f"""You work as a prompt and AI teacher. Your task is to ensure that the user gives a correct prompt to an AI. The current requirements for the user prompt are: {PROMPT_REQUIREMENTS} If the prompt is too vague and doesn't include the request information return BAD_PROMPT. If the prompt is correct return GOOD_PROMPT."""


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


@pytest.mark.it(PROMPT_REQUIREMENTS)
def test_prompt():
    from app import PROMPT
    result = create_prompt(TESTER_PROMPT, PROMPT)


    # Save the result in a file response.txt
    with open("response.txt", "w") as f:
        f.write(result)

    assert "GOOD_PROMPT" in result
