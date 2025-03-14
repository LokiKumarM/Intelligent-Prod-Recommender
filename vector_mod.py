from langchain_huggingface import HuggingFaceEmbeddings
import uuid
import chromadb
from langchain_chroma import Chroma
import json
import api_req

def vector_func(user_query):
    search_result = api_req.search_res(user_query)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    unique_collection_name = f"collection_{uuid.uuid4()}"

    client = chromadb.Client()
    collection = client.get_or_create_collection(name=unique_collection_name)

    for items in search_result:
        collection.add(
            documents=str(items),
            ids=[str(uuid.uuid4())]
        )

    vector_store_from_client = Chroma(
        client=client,
        collection_name="my_collections",
        embedding_function=embeddings
    )

    retriever = vector_store_from_client.similarity_search_with_score(user_query,k=6)

    documents_dict = [
        {"page_content": doc.page_content, "metadata": doc.metadata} for doc,_ in retriever
    ]
    ret_json = json.dumps(documents_dict)
    return ret_json