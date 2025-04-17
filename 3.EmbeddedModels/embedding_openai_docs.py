# here i'm working for generating query of single vector 


from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "Washington D.C is the capital of USA"
]

result = embedding.embed_documents(documents)

print(str(result))