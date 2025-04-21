from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables (your OpenAI API key, etc.)
load_dotenv()

# Initialize the model
model = ChatOpenAI()

# Set up Streamlit
st.header('Research Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )



# Set up the LLM chain
chain = LLMChain(llm=model, prompt=prompt)

# When the button is clicked, generate the summary
if st.button('Summarize'):
    result = chain.run({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result)
