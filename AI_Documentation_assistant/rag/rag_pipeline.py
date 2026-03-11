from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_groq import ChatGroq
from opentelemetry import context


VECTORSTORE_PATH = "vector_store"


# ------------------------------
# LOAD VECTOR STORE
# ------------------------------

def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


# ------------------------------
# RETRIEVE CONTEXT
# ------------------------------

def retrieve_context(query):

    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])



# ------------------------------
# GENERATE RESPONSE WITH RAG
# ------------------------------

def generate_with_rag(user_input, groq_api_key):

    context = retrieve_context(user_input)

    llm = ChatGroq(
        api_key=groq_api_key,
        model="openai/gpt-oss-20b"
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an expert analytics documentation assistant.

Use the provided company documentation context to help explain or document the user input.

Company Documentation Context:
{context}

User Input:
{user_input}

Generate clear structured documentation.
"""
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "context": context,
        "user_input": user_input
    })

    return response
