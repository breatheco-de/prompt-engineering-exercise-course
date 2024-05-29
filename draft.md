**General requirements**: All the READs should be written in a friendly and engaging tone, making the content easy to understand for users with different levels of expertise in the subject matter. The goal is to provide clear and concise explanations, examples, and instructions to help users learn about the topic and apply their knowledge effectively. It should be markdown formatted, including the title of the READ at the top of the document and a related emoji. This is an example of how the READs should be structured:

```markdown
# Title of the READ

An introductory paragraph for the READ, providing an overview of the topic and what users can expect to learn.

## Subtitle 1

Explanation of the first concept, including relevant information, examples, and tips to help users understand the topic better. If possible, external resources or references can be included to provide further information.

## Subtitle 2

The same structure as above should be followed for each concept or section covered in the READ.

## Instructions 📌

If the read includes instructions or tasks for the user to complete, they should be clearly outlined in this section. Each task should have a brief description of what the user needs to do and any specific requirements or guidelines to follow.
```

## Exercise Requirements


<!-- ### 05 - Let the Model Think
Teach the user how to create prompts that encourage the AI to "think" or process information before generating a response.

### 05.1 - Improve Accuracy in Physics Prompt
**Task:** Instruct the user on how to refine a physics-related prompt to get more accurate and detailed explanations from the AI. -->

### 06 - Some Shots Prompts

- Explain zero-shot, one shot, few shots and many shots.
- Explain why giving examples in prompts can help the AI generate more accurate and relevant outputs
- Explain the concept of "shots" in prompting.

### 06.1 - Obtaining a Correct List of Products

We have this text with the following products:

```markdown
### Notebooks

A versatile tool for jotting down notes, ideas, and sketches. Each notebook costs $5.99. 4 out of 5 customers think the notebooks are a great option for their business. Product code: ntb-001.

### Pens

High-quality pens designed for smooth writing and durability. Each pen costs $1.99. 5 out of 5 customers recommend these pens for their reliability and comfort. Product code: pen-002.

### Microphone

A professional-grade microphone ideal for recording, streaming, and online meetings. Each microphone costs $49.99. 4.5 out of 5 customers praise the microphone for its clear sound quality and ease of use. Product code: mic-003.
```

But we want to improve our guide to get a easier way to read the products' list. We need a guide that includes for each product: name, price, customer rating, and product code in a format like:

```markdown
- **Notebooks**
  - Price: $5.99
  - Customer Rating: 4 out of 5
  - Product Code: ntb-001
```

**Task for user:** CReate a prompt to get a correct list of products in the desired format.

### 


### 07.1 - Become a Superhero

**Task for user**: Create a prompt to generate a story about a superhero with specific powers and a mission to save the world. The super hero should be based in yourself, include enough context to avoid hallucinations.
