# retriever.py
import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
persist_dir = os.getenv("VECTOR_DATABASE_PATH")

def get_relevant_reports(query, n_results=3):
    client = chromadb.PersistentClient(path=persist_dir)
    embedding_fn = OpenAIEmbeddingFunction(api_key=OPENAI_API_KEY)
    collection = client.get_collection(name="reports", embedding_function=embedding_fn)
    
    results = collection.query(query_texts=[query], n_results=n_results)
    return results

# Example of what the results variable looks like when n_results=3:
# {
#     "ids": [["id_7", "id_12", "id_2"]],
#     "documents": [["the report description", ...]],
#     "metadatas": [[{"name": "Report A"}, {"name": "Report B"}, ...]]
# }

if __name__ == "__main__":
    print("🔍 Testing retrieval from vector database...")

    try:
        # Example query
        user_query = input("Enter a test query to find matching reports: ")

        # Run the retrieval function
        results = get_relevant_reports(user_query, n_results=3)

        # Print results nicely
        print("\n📊 Top matching reports:\n")
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            print(f"📌 Report Name: {meta['name']}")
            print(f"📝 Description: {doc}")
            print("-" * 50)

    except Exception as e:
        print("❌ Error during retrieval test:")
        print(e)
