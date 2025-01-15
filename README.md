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

# Using fruitstand

There are 2 steps to running tests using fruitstand. The first step is creating a baseline, this runs queries against a specific LLM and model. If you are currently using and LLM with a specific model, this should be your baseline. Creating a baseline will let you know that if you switch models, you can expect a similar response. Doing this immediately will also allow you to test for model degridation.

Once you have your baseline, you can test other LLMs and models against it. These tests will allow you to know that you can switch models without any developed functionality from being negatively impacted.

## Running command line

### Baseline

#### Arguments:

- -f, --filename: File containing test data (required).
- -o, --output: Directory to store baseline data (required).
- -qllm: LLM to generate baseline queries for (required).
- -qm, --model: Model for the query LLM (required).
- -qkey: API key for querying the LLM (required).
- -ellm: LLM for generating embeddings (required).
- -em: Model for generating embeddings (required).
- -ekey: API key for the embeddings LLM (required).

#### Example

```
fruitstand baseline -o ./baseline -f ./data/test_data.json -qllm openai -qm "gpt-4o-mini" -qkey sk-******** -ellm openai -em text-embedding-3-large -ekey sk--********
```

### Test

#### Arguments:

- -b, --baseline: File containing baseline data (required).
- -f, --filename: File containing test data (required).
- -o, --output: Directory to store test results (required).
- -llm: LLM to run queries against (required).
- -m, --model: Model for the query LLM (required).
- -qkey: API key for querying the LLM (required).
- -ekey: API key for the embeddings LLM (must match baseline’s embeddings LLM) (required).
- -threshold: Similarity threshold to determine test success (required, float).

#### Example

```
fruitstand test -b ./baseline/baseline__openai_gpt-4o-mini__openai_text-embedding-3-large__1736980847061344.json -o ./test_results data -f ./data/test_data.json -llm openai -m "gpt-4o-mini" -qkey sk-******** -ekey sk--******** -threshold 0.85
```
