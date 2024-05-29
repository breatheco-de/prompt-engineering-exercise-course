# 06.1 - Obtaining a correct list of products

Now that you've learned about the different types of shots in prompting, let's put your skills to the test with a practical exercise.

### Scenario
Imagine that you and me are working on a product guide for an online store. We have a list of products with their descriptions, prices, and customer ratings. However, the current format is not very user-friendly, and we need to improve it to make it easier to read and understand.

This is the current format of the product list:

```markdown
### Notebooks

A versatile tool for jotting down notes, ideas, and sketches. Each notebook costs $5.99. 4 out of 5 customers think the notebooks are a great option for their business. Product code: ntb-001.

### Pens

High-quality pens designed for smooth writing and durability. Each pen costs $1.99. 5 out of 5 customers recommend these pens for their reliability and comfort. Product code: pen-002.

### Microphone

A professional-grade microphone ideal for recording, streaming, and online meetings. Each microphone costs $49.99. 4.5 out of 5 customers praise the microphone for its clear sound quality and ease of use. Product code: mic-003.
```

## Instructions 📌
We want to improve our guide to get a easier way to read the products' list. We need a guide that includes for each product: name, price, customer rating, and product code in a format like:

```markdown
- **Notebooks**
  - Price: $5.99
  - Customer Rating: 4 out of 5
  - Product Code: ntb-001
```

Your task is to create a prompt that will help us obtain a correct list of products in the desired format. Remember to use the appropriate delimiters and provide clear instructions for the AI to understand the task. Use one of following shots: one-shot, few-shot, or many-shot, depending of the number of examples you think the AI needs to understand the task.