# AI Documentation Assistant

An AI-powered tool that automatically generates professional documentation for data analytics work.

This project uses **Retrieval Augmented Generation (RAG)** to combine internal data architecture documentation with LLM reasoning to produce structured explanations.

Built with:

- LangChain
- Groq LLMs
- Streamlit
- Chroma Vector Database

---

# Features

### 1️⃣ SQL Query Documentation
Automatically explains SQL queries by analyzing logic and referencing table definitions.

Example output includes:
- Query Objective
- Tables Used
- Transformation Logic
- Metrics Generated

---

### 2️⃣ Python / Notebook Documentation
Generates clean explanations of analytics notebooks including:
- Data loading
- Transformations
- Modeling steps
- Outputs

---

### 3️⃣ Experiment Documentation
Converts raw experiment results into structured reports:

- Experiment Objective
- Experiment Setup
- Metrics Evaluated
- Statistical Significance
- Business Recommendation

---

# Architecture

User Input
↓
Streamlit UI
↓
Documentation Generator
↓
RAG Pipeline
↓
Vector Database (Company Docs)
↓
Groq LLM
↓
Generated Documentation


---

# Project Structure
AI-Documentation-Assistant
│
├── app
├── data_architecture_docs
├── generators
├── rag
├── vectorstore



---

# Installation

Clone the repository:



git clone https://github.com/AKASHC1297/GenAI_Projects/AI-Documentation-Assistant.git

cd AI-Documentation-Assistant


Create environment:



python -m venv venv


Activate environment:

Mac/Linux



source venv/bin/activate


Windows



venv\Scripts\activate


Install dependencies:



pip install -r requirements.txt


---

# Setup Environment Variables

Create a `.env` file:



GROQ_API_KEY=*your_groq_api_key*


---

# Build the Vector Database

Run:



python scripts/build_vectorstore.py


---

# Run the Application



streamlit run app/app.py


---

# Example Use Cases

### SQL Documentation

Input:



SELECT rider_id, COUNT(*) AS trips
FROM fact_trip
GROUP BY rider_id


Output:



Query Objective
Tables Used
Metrics Generated
Transformation Logic


---

# Future Improvements

- Automatic SQL table extraction
- File upload support (.sql, .ipynb)
- PDF documentation export
- Multi-agent documentation system

---

# Author

Akash Chakraborty
