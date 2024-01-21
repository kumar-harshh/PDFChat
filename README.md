# Retrieval-Augmented Generation (RAG) Using Cohere, Lanchain & FAISS Vector DB: Chat with Multiple PDFs 🚀

# PDFChat-Your Personal Chat Bot
This project enables you to engage in a conversation with multiple PDF documents. The chatbot is designed to process uploaded PDFs, extract text, generate embeddings, and provide a conversational experience based on the content of the PDFs.

## How to Use

1. **Ensure PDF Upload:**
   - Upload your PDF files using the sidebar. Click on "Select your PDF files & Click on 'Process' to proceed."

2. **Ask Questions:**
   - After uploading the PDFs, a text input field will appear. Enter your questions in the text input.

3. **Chat Interface:**
   - The chatbot will respond to your questions based on the content of the processed PDFs.
   - The conversation history is displayed in the main area, showing both user and bot messages.

## Setup

### Requirements

- Streamlit
- PyPDF2
- langchain
- langchain_community
- Cohere
- FAISS
- dotenv

### Installation

1. Clone the repository:

   ```bash
   git@github.com:kumar-harshh/PDFChat.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Environment Variables:

   - Create a `.env` file in the project root.
   - Add your Cohere API key to the `.env` file:

     ```
     COHERE_API_KEY=your_cohere_api_key_here
     ```
    - If you don't have an API Key, You can generate one from Cohere's site: https://dashboard.cohere.com/api-keys
4. Run the application:

   ```bash
   streamlit run main.py
   ```

## Features

- **PDF Processing:**
  - Extracts text from uploaded PDFs using PyPDF2.
  - Divides the text into chunks using langchain text splitter.

- **Embeddings:**
  - Generates embeddings for text chunks using Cohere embeddings.
  - Stores embeddings in the Vector Database using FAISS.

- **Conversational AI:**
  - Utilizes langchain to create a conversational chain.
  - Maintains a chat history to provide context-aware responses.

## Notes

- This project leverages Streamlit for the web interface and integrates several Python libraries for PDF processing, text embedding, and chatbot functionalities.

- This Project is using free API Keys hence the token size of response is rate limited.

- Make sure to upload the PDF files before asking questions to enable the chatbot to provide meaningful responses.

Feel free to explore, ask questions, and enhance the project further! 🚀
