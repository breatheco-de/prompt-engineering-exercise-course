import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from prompt import create_prompt

def main():
    system_message = "You are an useful assistant"
    user_message = "I'd like to know more about AI development"
    response = create_prompt(system_message, user_message)
    # Print this in green
    print("\033[92m" + response + "\033[0m")

    # Save the response in a .txt file
    with open("response.txt", "w") as f:
        f.write(response)
    

main()