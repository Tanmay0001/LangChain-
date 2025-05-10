'''webbase loader generally we used it to load and extract text content from the webpages(URLs)'''

from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text -\n {text}',
    input_variables=['question', 'text']
)
parser = StrOutputParser()
url = 'https://resho.in/product/boat-rockerz-510-bluetooth-ear-headphone/'
loader = WebBaseLoader(url)


docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the price of this product?', 'text':docs[0].page_content}))