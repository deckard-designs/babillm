# Why is this library called fruitstand?

Because we’re comparing apples and oranges! Most testing involves checking that a value returned from a function is the same as what is expected. This doesn’t work when working with LLMs, as they are nondeterministic. Therefore, you need to check that there is a threshold of similarity.

# Why would I want to use this library?

If you’re using a particular LLM model prompt to determine an action based on the response, you may want to ensure that a response has a certain similarity when transitioning between models. This library allows you to set a baseline with the current model and verify that upgrading or changing models maintains the same behavior.

For example, you are using an LLM to do intent detection for your chatbot. You have a prompt like this:

```
Based on the provided user prompt, determine if the user wanted to:
1. Change their address
2. Change their name
3. Cancel their subscription

User Prompt:
I would like to update my subscription.
```

Using fruitstand will ensure that the LLM routes to the correct intent as you upgrade/change your llm/model.
