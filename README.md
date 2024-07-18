---

## QueryXpertAI
#Supervized-Fine tuning transformer based modal with Streamlit Integration


### Overview

QueryXpertAI is an interactive document-based question-answering system. Leveraging advanced natural language processing (NLP) models from Hugging Face and sophisticated document handling with LangChain, this application allows users to upload PDF documents and query their content seamlessly. The system is designed for easy deployment on Streamlit Cloud, providing an intuitive interface for document analysis and information retrieval.

### Features

- **PDF Document Upload**: Securely upload PDF files for analysis.
- **Advanced NLP Models**: Utilizes Hugging Face's cutting-edge language models for precise question answering.
- **Streamlit Integration**: A user-friendly interface powered by Streamlit for seamless interaction.
- **Chunked Document Processing**: Efficiently splits documents into manageable chunks for better processing.
- **Embeddings & Vector Storage**: Uses Hugging Face Embeddings and Chroma for effective vector storage and retrieval.
- **Real-time Querying**: Instant answers to your queries about the uploaded documents.

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yashn24/queryexpertai.git
   cd queryexpertai
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   - Set your Hugging Face API token in the environment variable `HUGGINGFACEHUB_API_TOKEN`.

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

### Deployment on Streamlit Cloud

1. **Ensure your project includes:**
   - `app.py`
   - `requirements.txt`

2. **Deploy on Streamlit Cloud**
   - Push your repository to GitHub.
   - Deploy directly from your GitHub repository on Streamlit Cloud.

### Usage

1. Open the deployed Streamlit app.
2. Enter your Hugging Face API token.
3. Upload a PDF document.
4. Type in your query and get instant answers from the document.

### Example

1. **Upload a PDF**: Select and upload your PDF file.
2. **Ask a Question**: Type in any question related to the document content.
3. **Receive an Answer**: The system will process the query and return the relevant answer along with the content page of the context asked.

### Contribution

We welcome contributions! Please fork the repository and create a pull request with your changes. Make sure to follow the project's coding standards and include relevant tests.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Contact

For any questions or issues, please open an issue in the repository or contact us directly.

---
