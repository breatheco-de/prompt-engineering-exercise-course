### About Context and Hallucinations 🧠

The importance of context in prompt creation is undeniable. In this lesson, we will explore what context is, how to provide enough context to obtain accurate and relevant outputs from the AI, and how to avoid **hallucinations**.

### Understanding Context in Prompt Creation 📚

Context is crucial when interacting with AI models. It helps the AI understand the background and specific details of your request, leading to more accurate and relevant responses.

If you do not provide enough context, the AI might generate irrelevant or incorrect information, which can also lead to hallucinations where the AI generates information that is not accurate or relevant.

### What are Hallucinations? 😵‍💫

A hallucination occurs when the AI generates information that is not true because it does not have enough context or the training data does not include the specific information you are requesting.

#### Bad Prompt:
```text
What was the magnitude of the earthquake that occurred on April 3, 2024, in Taiwan? How many people were injured?
```
This prompt lacks context and could lead to inaccurate or irrelevant responses because the training data might not include this specific event.

#### Good Prompt:
```text
What was the magnitude of the earthquake that occurred on April 3, 2024, in Taiwan? How many people were injured?

Context from Wikipedia: On April 3, 2024, at 07:58:11 NST (23:58:11 UTC on April 2), a magnitude 7.4 earthquake struck 15 km (9.3 mi) south of Hualien City, Hualien County, Taiwan. At least 18 people died and more than 1,100 were injured in the earthquake. It is the strongest earthquake in Taiwan since the Jiji earthquake in 1999, with three aftershocks above magnitude 6.0.
```
In this prompt, we provide enough context about the earthquake in Taiwan, which will make the generated response not a hallucination.

#### Example of hallucination for the first prompt:
```text
The magnitude of the earthquake was 7.5 on the Richter scale and around 500 people were injured.
```

### Tips to Avoid Hallucinations 📝🚫

To ensure that the AI understands your request, you should:
1. **Be Specific**: Clearly state what you need.
2. **Provide Background Information**: Include any relevant details that can help the AI understand the context, remember to use delimiters appropriately.
3. **Use Examples**: If possible, provide examples to illustrate your point.
4. **Verify Information**: Always verify the AI's responses with reliable sources.
5. **Ask the AI** to indicate if it **does not** have enough information to answer your question.