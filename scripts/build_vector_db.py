# build_vector_db.py
import pandas as pd
import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv
import os
load_dotenv()

# This script builds a vector database from an Excel file containing report names and descriptions.
persist_dir_path = os.getenv("VECTOR_DATABASE_PATH")
persist_dir = os.path.abspath(persist_dir_path)
print(f"📁 Vectorstore will be saved in: {persist_dir}")

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Function to load data from an Excel file
# The Excel file should have two columns: "ReportName" and "Description"
def load_data(path):
    df = pd.read_excel(path)
    return df["ReportName"].tolist(), df["Description"].tolist()

def build_vector_db(names, descriptions):
    client = chromadb.PersistentClient(path=persist_dir)                # Ensures vector data is saved to directory persist_dir.
    embedding_fn = OpenAIEmbeddingFunction(api_key=OPENAI_API_KEY)      # Tells ChromaDB to use OpenAI’s embeddings under the hood using OpenAI API key.
    
    collection = client.get_or_create_collection(name="reports", embedding_function=embedding_fn) # A collection is like a “table” of embedded documents.
    
    collection.add(
        documents=descriptions,
        ids=[f"id_{i}" for i in range(len(descriptions))],
        metadatas=[{"name": name} for name in names]
    )
    
    # client.persist()

if __name__ == "__main__":
    names, descriptions = load_data("data/reports.xlsx")
    build_vector_db(names, descriptions)
    print("✅ Vector DB created and saved.")