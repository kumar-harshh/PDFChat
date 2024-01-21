import streamlit as st
from streamlit_lottie import st_lottie
import PyPDF2 as pdf
from langchain.text_splitter import CharacterTextSplitter as ct
from langchain.embeddings.cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Cohere
from chatbot_style import css, bot_template, user_template
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("COHERE_API_KEY")

#To persist the conversation context
def get_conversation_chain(vector_store):
    llm=Cohere(model="command")
    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True, human_prefix="Human", ai_prefix="Bot")
    conversation_chain=ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
    )
    return conversation_chain
    

st.title("Chat with multiple PDFs 👋🏻")
st.write("You Must Ensure that you have uploaded the PDF files before asking a question")
with open('animation.json') as anim_source:
    animation = json.load(anim_source)
st_lottie(animation, 1, True, True, "high", 350, -200)

question=st.text_input("Hi! How May I Help?")

#Initialising Sesson States
if "conversation" not in st.session_state:
    st.session_state.conversation=None
if "chat_history" not in st.session_state:
    st.session_state.chat_history=None
    
#Process Flow-> Upload PDF-> Extract Text -> Chunk them up-> Generate Embeddings->
# -> Store them in the Vector DB -> Chat Chain

st.write(css, unsafe_allow_html=True)

if question:
    response=st.session_state.conversation({"question":question})
    st.session_state.chat_history=response["chat_history"]
    for i, message in enumerate(st.session_state.chat_history):
        if i%2==0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

                    
    
with st.sidebar:
    st.header("Upload your PDFs 📚")
    doc_pdf_files=st.file_uploader("Select your PDF files & Click on 'Process' to proceed", accept_multiple_files=True)
    submit=st.button("Process")
    if submit:
        with st.spinner("Processing! Wait a While...."):
            #Extract PDF text-Using PyPDF2 pdfreader method
            text = ""
            for file in doc_pdf_files:
                reader = pdf.PdfReader(file)
                for page_number in range(len(reader.pages)):
                    page = reader.pages[page_number]
                    text += str(page.extract_text())
            
            
            #Chunk them up- Text Chunking using langchain textsplitter
            text_chunker= ct(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
                add_start_index = True
            )
            text_chunk=text_chunker.split_text(text)
                        
            #Create Embeddings & Store them in the Vector Database
            embeddings = CohereEmbeddings(model="embed-english-light-v3.0")
            vector_store=FAISS.from_texts(texts=text_chunk, embedding=embeddings)
            
            if embeddings:
                st.write("✅ File is Uploaded & Embeded, You may ask your questions now")
            else:
                st.write("❗️ Failed to process the Document")
                
            #Create Chat Buffer Memory using langchain
            st.session_state.conversation=get_conversation_chain(vector_store)

