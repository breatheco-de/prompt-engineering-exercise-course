# -*- coding: utf-8 -*-
import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))
from prompt import create_prompt


PROMPT = "What happened in recent days with the Google algorithm?"

# Generations will be added below this line


# DO NOT CHANGE THIS CODE
GENERATIONS = 0
system_prompt = "You are an useful assistant"
def main():
    global GENERATIONS
    response = create_prompt(system_prompt, PROMPT)

    
    # Read the current file content
    with open(__file__, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find the current number of generations
    generation_matches = re.findall(r'AI_RESPONSE_\d+', content)
    if generation_matches:
        GENERATIONS = max(int(match.split('_')[-1]) for match in generation_matches) + 1
    
    # Insert the new response at the specified line
    insert_line = "# Generations will be added below this line\n"
    new_content = content.replace(insert_line, f'{insert_line}\nAI_RESPONSE_{GENERATIONS} = """{response}"""\n')
    
    # Write the updated content back to the file
    with open(__file__, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    return response

if __name__ == "__main__":
    main()
