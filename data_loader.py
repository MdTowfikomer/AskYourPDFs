# from http.client import responses
import cohere
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os

load_dotenv()

# Cohere client
client =  cohere.Client(api_key=os.getenv("COHERE_API_KEY"))

EMBED_MODEL = "embed-multilingual-v3.0"
EMBED_DIM = 1024 # Cohere multilingual v3 dimension


splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

# reading the doc
# Searching in doc 
def embed_texts(texts: str | list[str], input_type="search_document") -> list[float] | list[list[float]]:
    
    single_input = False
    if isinstance(texts, str):
        texts = [texts]
        single_input = True
    
    response = client.embed(
        texts=texts,
        model=EMBED_MODEL,
        input_type=input_type,
    )
    
    embeddings = response.embeddings
    
    if single_input:
        return embeddings[0] # Return a single embedding
    return response.embeddings


