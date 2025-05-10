from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
docs = loader.load()


splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0, # betn 2 chunks the overlap is there, to put context similar infomation to lost less info.
    separator=''

)

result = splitter.split_documents(docs)

print(result[0])