import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from generators.sql_doc_generator import generate_sql_documentation
from generators.notebook_doc_generator import generate_notebook_documentation
from generators.experiment_doc_generator import generate_experiment_documentation


# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="AI Analytics Documentation Assistant",
    page_icon="📊",
    layout="wide"
)


# --------------------------------
# TITLE
# --------------------------------

st.title("AI Analytics Documentation Assistant")

st.markdown(
"""
Generate professional documentation for:

• SQL Queries  
• Python / Notebook Code  
• Experiment Results  

Powered by **RAG + LLMs**.
"""
)


# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("Configuration")

groq_api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password"
)


# --------------------------------
# TASK SELECTION
# --------------------------------

task = st.selectbox(
    "Select Documentation Task",
    [
        "SQL Query Documentation",
        "Python Notebook Documentation",
        "Experiment Results Documentation"
    ]
)


# --------------------------------
# SQL DOCUMENTATION
# --------------------------------

if task == "SQL Query Documentation":

    st.subheader("Enter SQL Query")

    sql_query = st.text_area(
        "Paste your SQL query here",
        height=200
    )

    if st.button("Generate SQL Documentation"):

        if not groq_api_key:
            st.error("Please provide your Groq API key.")
        elif not sql_query:
            st.error("Please enter a SQL query.")
        else:

            with st.spinner("Generating documentation..."):

                documentation = generate_sql_documentation(
                    sql_query,
                    groq_api_key
                )

            st.markdown("---")
            st.markdown(documentation)


# --------------------------------
# NOTEBOOK DOCUMENTATION
# --------------------------------

elif task == "Python Notebook Documentation":

    st.subheader("Enter Python / Notebook Code")

    notebook_code = st.text_area(
        "Paste your Python code here",
        height=200
    )

    if st.button("Generate Notebook Documentation"):

        if not groq_api_key:
            st.error("Please provide your Groq API key.")
        elif not notebook_code:
            st.error("Please enter Python code.")
        else:

            with st.spinner("Generating documentation..."):

                documentation = generate_notebook_documentation(
                    notebook_code,
                    groq_api_key
                )

            st.markdown("---")
            st.markdown(documentation)


# --------------------------------
# EXPERIMENT DOCUMENTATION
# --------------------------------

elif task == "Experiment Results Documentation":

    st.subheader("Enter Experiment Results")

    experiment_input = st.text_area(
        "Paste experiment results here",
        height=200
    )

    if st.button("Generate Experiment Documentation"):

        if not groq_api_key:
            st.error("Please provide your Groq API key.")
        elif not experiment_input:
            st.error("Please enter experiment results.")
        else:

            with st.spinner("Generating documentation..."):

                documentation = generate_experiment_documentation(
                    experiment_input,
                    groq_api_key
                )

            st.markdown("---")
            st.markdown(documentation)
