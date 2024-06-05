# -*- coding: utf-8 -*-
import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'utils')))
from prompt import create_prompt

# You can write multiple lines in the prompt :)
PROMPT = """Give a list of products that are available in the store.

This is the current product list:
'''
### Notebooks

A versatile tool for jotting down notes, ideas, and sketches. Each notebook costs $5.99. 4 out of 5 customers think the notebooks are a great option for their business. Product code: ntb-001.

### Pens

High-quality pens designed for smooth and durable writing. Each pen costs $1.99. 5 out of 5 customers recommend these pens for their reliability and comfort. Product code: pen-002.

### Microphone

A professional-grade microphone ideal for recording, streaming, and online meetings. Each microphone costs $49.99. 4.5 out of 5 customers praise the microphone for its clear sound quality and ease of use. Product code: mic-003.
'''


I want this format
'''
- **Notebooks**
  - Price: $5.99
  - Customer Rating: 4 out of 5
  - Product Code: ntb-001
'''
"""

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
