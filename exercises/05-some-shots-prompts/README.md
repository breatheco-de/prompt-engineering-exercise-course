### What are "Shots" in Prompt Creation? 🎬

In the context of AI and machine learning, "shots" refer to the number of examples provided to the model to help it understand the task. Let's break down the different types:

#### Zero-Shot Prompting

Zero-shot prompting means giving the AI a task without any example. The AI has to rely solely on its pre-existing knowledge and instructions to generate a response.

**Example:**
```text
Generate a JSON object that represents a user
```

#### One-Shot Prompting

One-shot prompting involves providing the AI with one example to help it better understand the task.

**Example:**
```text
Generate a JSON object that represents a user
Example: """
{
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}
"""
```
> **Hint:** Remember to use delimiters 👀.

#### Few-Shot Prompting

Few-shot prompting means giving the AI a few examples to improve its understanding of the task.

> Note: Generally, for large language models, it is not necessary to give many examples to understand a pattern; usually, 2 or 3 examples are sufficient depending on the complexity of the task.

**Example:**
```text
Generate a movie dialogue for a romantic comedy. There are two characters, Alice and Robert, who are childhood friends and fall in love.

Examples:
<Alice>: I've always had a crush on you, Robert.
<Robert>: I never knew, Alice. I feel the same way.

The scene ends with them holding hands and looking into each other's eyes.
```

#### Many-Shot Prompting

Many-shot prompting involves providing the AI with many examples. This is often used when the task is complex and requires more context and examples to be understood.

### Why Examples Help 🧩

Providing examples in prompts can significantly improve the performance of the AI. Here are some reasons why:

1. **Contextual Understanding:** Examples give the AI a better understanding of the task by providing context.
2. **Pattern Recognition:** The AI can recognize patterns in the examples and apply them to generate more accurate responses.
3. **Reduction of Ambiguity:** Examples help reduce ambiguity, making it easier for the AI to understand what is expected.

## TIPS 🤖

1. Experiment with different types of prompts (zero-shot, one-shot, few-shot, and many-shot) using the provided examples.
2. Observe how the AI's responses change with the number of examples given.
3. Try creating your own prompts for different tasks and see how providing examples affects the output.

Let's put into practice what you've learned about "shots" in prompt creation! 🚀