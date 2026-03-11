import os

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# -----------------------------
# PATH CONFIG
# -----------------------------

DOCS_PATH = "data_architecture_docs"
VECTORSTORE_PATH = "vector_store"


# -----------------------------
# LOAD DOCUMENTS
# -----------------------------

def load_documents():

    loader = DirectoryLoader(
        DOCS_PATH,
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    return documents


# -----------------------------
# ADD METADATA
# -----------------------------

def enrich_metadata(documents):

    for doc in documents:

        file_path = doc.metadata["source"]
        file_name = os.path.basename(file_path)

        doc.metadata["document_name"] = file_name

        if "dim_" in file_name or "fct_" in file_name or "fact_" in file_name:
            doc.metadata["doc_type"] = "table_schema"

        elif "metric" in file_name:
            doc.metadata["doc_type"] = "metric_definition"

        elif "business" in file_name:
            doc.metadata["doc_type"] = "business_logic"

        else:
            doc.metadata["doc_type"] = "general_doc"

    return documents


# -----------------------------
# SPLIT DOCUMENTS
# -----------------------------

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    split_docs = text_splitter.split_documents(documents)

    print(f"Split into {len(split_docs)} chunks")

    return split_docs


# -----------------------------
# CREATE EMBEDDINGS
# -----------------------------

def create_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


# -----------------------------
# BUILD VECTOR STORE
# -----------------------------

def build_vectorstore():

    print("Loading documents...")

    documents = load_documents()

    documents = enrich_metadata(documents)

    docs = split_documents(documents)

    print("Creating embeddings...")

    embeddings = create_embeddings()

    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )

    print("Saving vector store...")

    vectorstore.save_local(VECTORSTORE_PATH)

    print("Vector store built successfully!")


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    build_vectorstore()
