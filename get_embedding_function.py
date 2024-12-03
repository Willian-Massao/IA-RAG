from langchain_ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
import os

ollama_ip = os.getenv("OLLAMA_HOST", "http://192.168.15.6:11434")
ollama_model = os.getenv("OLLAMA_MODEL", "mistral")

def get_embedding_function():
    embeddings = OllamaEmbeddings(model=ollama_model, base_url=ollama_ip)
    return embeddings
