from rag.rag_pipeline import generate_with_rag


def generate_sql_documentation(sql_query, groq_api_key):

    prompt =f"""
You are a senior analytics engineer responsible for documenting SQL queries.

Return the documentation EXACTLY in the following markdown format.

Do not add extra sections.

---

## Query Objective
<Explain what the query does>

## Tables Used
<List tables and their purpose>

## Fields Used
<List fields and their description>

## Logic Explanation
<Explain the SQL logic step-by-step>

## Metrics Generated
<List metrics derived from the query>

## Business Interpretation
<Explain how the output is useful for business decisions>

---

SQL Query:
{sql_query}

I REPEAT! DO NOT Add extra sections. Follow the format EXACTLY as specified above.
"""

    documentation = generate_with_rag(
        user_input=prompt,
        groq_api_key=groq_api_key
    )

    return documentation
