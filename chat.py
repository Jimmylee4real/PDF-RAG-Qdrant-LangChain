from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()

# Vector Embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# take user input
user_query = input("Enter your question: ")

# Relevant chunks from the vector DB
search_results = vector_store.similarity_search(query=user_query)

context = "\n\n\n".join(
    [
        "Page Content: {content}\nPage Number: {page}\nSource File: {src}".format(
            content=result.page_content,
            page=result.metadata.get("page_label", "N/A"),
            src=Path(result.metadata.get("source", "")).name or "N/A",
        )
        for result in search_results
    ]
)

SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers user query based on the available
context retrieved from a PDF file along with page_contents and page number.

You should only answer the user based on the following context and navigate the
user to open the right page number to know more.

Context:
{context}

"""

response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ]
)

print(f"AI Assistant: {response.choices[0].message.content}")