# Some Shots Prompts 🎯

Let's dive into the concept of "shots" in prompting. You'll learn about zero-shot, one-shot, few-shot, and many-shot prompts, and understand why providing examples can help the AI generate more accurate and relevant outputs.

### What are "Shots" in Prompting? 🎬

In the context of AI and machine learning, "shots" refer to the number of examples provided to the model to help it understand the task. Let's break down the different types:

#### Zero-Shot Prompting

Zero-shot prompting means giving the AI a task without any examples. The AI has to rely solely on its pre-existing knowledge to generate a response.

**Example:**

```text
Generate a JSON object representing a user
```

#### One-Shot Prompting

One-shot prompting involves providing the AI with one example to help it understand the task better.

**Example:**

```text
Generate a JSON object representing an user
Example:
"""
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

**Example:**

```text
Generate a movie dialogue for a romantic comedy. There are two characters, Alice and Bob, who are childhood friends that fall in love.

Examples:
<Alice>: I've always had a crush on you, Bob.
<Bob>: I never knew, Alice. I feel the same way.

The scene ends with them holding hands and looking into each other's eyes.
```

#### Many-Shot Prompting

Many-shot prompting involves providing the AI with many examples. This is often used when the task is complex and requires more context.

**Example:**

```text
I want to make a list of fruits, vitamins and a recipe for each one. The following is an example of how the list should look:
* APPLE 🍎:
    - Vitamins: A, C
    - Recipe: Apple Pie

* BANANA 🍌
    - Vitamins: B6, C
    - Recipe: Banana Bread

Complete the list with at least 5 more fruits.
```

### Why Examples Help 🧩

Providing examples in prompts can significantly improve the AI's performance. Here are a few reasons why:

1. **Contextual Understanding:** Examples give the AI a better understanding of the task by providing context.
2. **Pattern Recognition:** The AI can recognize patterns in the examples and apply them to generate more accurate responses.
3. **Reduced Ambiguity:** Examples help reduce ambiguity, making it easier for the AI to understand what is expected.

## HINTS 🤖

1. Experiment with different types of prompts (zero-shot, one-shot, few-shot, and many-shot) using the examples provided.
2. Observe how the AI's responses change with the number of examples given.
3. Try creating your own prompts for different tasks and see how providing examples affects the output.

Happy prompting! ;p