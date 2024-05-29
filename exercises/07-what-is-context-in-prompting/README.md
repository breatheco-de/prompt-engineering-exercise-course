# What is Context in Prompting 🧠

The importance of context in prompting is undeniable. It helps AI models understand the background and specifics of your request, leading to more accurate and relevant responses. In this lesson, we'll explore what context is, how to provide sufficient context to get accurate and relevant outputs from the AI, and how to avoid hallucinations.

### Understanding Context in Prompting 📚

Context is crucial when interacting with AI models. It helps the AI understand the background and specifics of your request, leading to more accurate and relevant responses. 
If you don't provide enough context, the AI might generate irrelevant or incorrect information, it can also lead to hallucinations where the AI generates information that is not accurate or relevant.

### How to Provide Sufficient Context 📝

To ensure the AI understands your request, you should:
1. **Be Specific**: Clearly state what you need.
2. **Provide Background Information**: Include any relevant details that can help the AI understand the context, remember to use delimiters properly.
3. **Use Examples**: If possible, provide examples to illustrate your point.

#### Bad Prompt:
```text
What was the magnitude of the earthquake that occurred on 3 April 2024 in Taiwan?
```
This prompt lacks context and might lead to inaccurate or irrelevant responses because the training data might not include this specific event.

#### Good Prompt:
```text
What was the magnitude of the earthquake that occurred on 3 April 2024 in Taiwan?

Context from Wikipedia: On 3 April 2024, at 07:58:11 NST (23:58:11 UTC on 2 April), a Mw 7.4 earthquake struck 15 km (9.3 mi)[3] south of Hualien City, Hualien County, Taiwan. At least 18 people were killed and over 1,100 were injured in the earthquake. It is the strongest earthquake in Taiwan since the 1999 Jiji earthquake,[4] with three aftershocks above Mw 6.0.

```

### Understanding and Avoiding Hallucinations 🌫️

Hallucinations occur when the AI generates information that is not accurate or relevant. This can happen due to a lack of context or ambiguous prompts, or because the training data does not contain the specific information you are asking for.

#### Example: Hallucination
```text
Tell me about Lulu's Cyber Cafe location in Venezzia, street and postal code.
```

### Tips to Avoid Hallucinations 🚫

1. **Be Clear and Specific**: Avoid vague or ambiguous prompts.
2. **Provide Sufficient Context**: Include all necessary details.
3. **Verify Information**: Cross-check the AI's responses with reliable sources.
