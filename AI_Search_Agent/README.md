# 🔎 AI Research Agent

An **Agentic AI-powered research assistant** built using **LangChain, LangGraph, Groq LLM, and Streamlit**.
The agent autonomously decides when to use external tools such as **DuckDuckGo Search, Wikipedia, and Arxiv** to gather information and generate well-informed answers.

This project demonstrates the implementation of a **ReAct-style agent architecture** capable of **tool selection, reasoning, and source-based response generation**.

---

# 🚀 Features

* **Agentic AI Architecture**
* **Multi-tool research capabilities**
* **Academic paper search via Arxiv**
* **Web search using DuckDuckGo**
* **Knowledge retrieval from Wikipedia**
* **ReAct reasoning (Thought → Action → Observation)**
* **Fast inference using Groq LLM**
* **Interactive chat interface via Streamlit**
* **Tool execution transparency**
* **Source attribution for responses**

---

#  System Architecture

```
User Query
    │
    ▼
Streamlit Chat Interface
    │
    ▼
LangGraph ReAct Agent
    │
    ├── DuckDuckGo Search
    ├── Wikipedia API
    └── Arxiv API
    │
    ▼
Context Retrieval
    │
    ▼
Groq LLM (openai/gpt-oss-20b)
    │
    ▼
Final Answer + Sources
```

---

#  Project Structure

```
AI-Search-Agent
│
├── app
│   └── app.py                # Streamlit application entry point
│
├── agents
│   └── search_agent.py       # ReAct agent construction
│
├── tools
│   └── tools.py              # Tool configuration (Arxiv, Wikipedia, DuckDuckGo)
│
├── ui
│   └── chat_ui.py            # Chat streaming interface
│
├── utils
│   └── config.py             # Environment configuration
│
├── requirements.txt
└── README.md
```

---

#  Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/GenAI_Projects.git
cd GenAI_Projects/AI-Search-Agent
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Environment Setup

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
```

You can get a Groq API key from:

https://console.groq.com

---

#  Running the Application

Run the Streamlit app:

```bash
streamlit run app/app.py
```

The application will launch locally at:

```
http://localhost:8501
```

---

# Example Queries

Try asking the agent questions such as:

```
What are the latest research papers on reinforcement learning?
```

```
Explain the Transformer architecture in deep learning
```

```
Who invented the CRISPR gene editing technique?
```

```
Find recent Arxiv papers about LLM reasoning
```

The agent will automatically decide which tool(s) to use.

---

# Tech Stack

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| **LangChain**      | LLM orchestration         |
| **LangGraph**      | Agent workflow engine     |
| **Groq LLM**       | High-speed inference      |
| **Streamlit**      | Interactive web interface |
| **DuckDuckGo API** | Web search                |
| **Wikipedia API**  | Knowledge retrieval       |
| **Arxiv API**      | Research paper search     |

---

# Example Agent Reasoning

```
User Query:
"What are the latest papers on diffusion models?"

Agent Thought:
Need academic sources → Query Arxiv

Tool Call:
Arxiv Search

Observation:
Relevant paper summaries retrieved

Final Response:
Summarized findings with references
```

---

# Learning Objectives

This project demonstrates:

* Agentic AI design patterns
* ReAct agent implementation
* Multi-tool LLM orchestration
* Tool selection reasoning
* Real-time LLM streaming
* Production-style project structuring

---

# Future Improvements

* Add **RAG memory system**
* Add **multi-step planning agent**
* Support **PDF research paper ingestion**
* Add **citation formatting**
* Deploy using **Docker + Streamlit Cloud**

---

# 👤 Author

**Akash Chakraborty**

