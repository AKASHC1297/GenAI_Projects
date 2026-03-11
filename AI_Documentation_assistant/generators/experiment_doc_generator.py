from rag.rag_pipeline import generate_with_rag


def generate_experiment_documentation(experiment_results, groq_api_key):

    prompt = f"""
You are a senior data scientist responsible for documenting product experiments.

Analyze the experiment results and generate a professional experiment report.

Return the documentation EXACTLY in the following markdown structure.

---

## Experiment Objective
<Explain what the experiment aims to test>

## Experiment Setup
<Explain control group, treatment group, and experiment design>

## Metrics Evaluated
<List the metrics used to evaluate the experiment>

## Results Summary
<Summarize the observed results>

## Statistical Significance
<Explain whether results are statistically significant and what the p-value indicates>

## Business Recommendation
<Provide a recommendation based on the results>

---

Experiment Results:
{experiment_results}

I REPEAT! DO NOT Add extra sections. Follow the format EXACTLY as specified above.
"""

    documentation = generate_with_rag(
        user_input=prompt,
        groq_api_key=groq_api_key
    )

    return documentation
