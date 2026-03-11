from rag.rag_pipeline import generate_with_rag


def generate_notebook_documentation(notebook_code, groq_api_key):

    prompt = f"""
You are a senior data analyst responsible for documenting Python analytics scripts and notebooks.

Analyze the provided Python code and generate structured documentation.

Return the documentation EXACTLY in the following markdown structure.

---

## Code Objective
<Explain the purpose of the code>

## Libraries Used
<List Python libraries and their purpose>

## Data Sources
<Explain tables, datasets, or inputs used>

## Step-by-Step Logic
<Explain the code workflow step-by-step>

## Outputs Generated
<Explain what outputs or metrics the script produces>

## Business Interpretation
<Explain the business value of the outputs>

---

Python Code:
{notebook_code}

I REPEAT! DO NOT Add extra sections. Follow the format EXACTLY as specified above.

"""

    documentation = generate_with_rag(
        user_input=prompt,
        groq_api_key=groq_api_key
    )

    return documentation
