# use pytest and ensure that there is an GROQ_API_KEY in the .env file
import os
from dotenv import load_dotenv
load_dotenv()

def test_api_key():
    with open(".env", "r") as f:
        lines = f.readlines()
        assert any("GROQ_API_KEY=" in line for line in lines)
    assert os.environ["GROQ_API_KEY"] is not None