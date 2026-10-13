# Multi-LLM AI Workspace

A Python-based Generative AI application that integrates multiple Large Language Models, including Google Gemini and Claude through OpenRouter. The project provides a unified workspace for AI-powered productivity, developer, document, research, and data science workflows.

🎯 Problem Statement

Using multiple AI models usually means switching between different websites, API keys, and interfaces. Working with documents (PDFs, reports, research material) adds more manual effort. This project brings multiple LLMs, document Q&A, and AI productivity tools into one workspace, so users can pick the right model for each task and get answers grounded in their own documents.

## 🚀 Key Features

- **Multi-LLM Integration** – Google Gemini and Claude via OpenRouter
- **LLM Routing** – Select and route requests to the required AI model
- **Conversational AI** – Interactive chat with session-based conversation memory
- **Research Assistant** – Generate structured research reports
- **RAG-based PDF Chat** – Ask questions from PDF documents using Retrieval-Augmented Generation
- **Document Q&A** – Semantic document search and question answering
- **Document Summarization** – Chunk-based document summarization
- **FAISS Vector Search** – Efficient similarity search over document embeddings
- **Embeddings** – Sentence Transformers for semantic representation
- **Developer AI Tools** – AI-assisted coding and development workflows
- **Data Science AI Tools** – AI-powered data analysis workflows
- **Prompt Library** – Reusable prompts for common AI tasks
- **Streamlit Interface** – Interactive user interface for AI tools

## 🛠️ Technologies

- **Python**
- **Generative AI**
- **Large Language Models (LLMs)**
- **Google Gemini API**
- **Claude / OpenRouter API**
- **Retrieval-Augmented Generation (RAG)**
- **FAISS**
- **Sentence Transformers**
- **Vector Embeddings**
- **Semantic Search**
- **REST API Integration**
- **Streamlit**
- **Git & GitHub**

## 🏗️ Architecture

                  
                         Multi-LLM AI Workspace
                                  │
                                  ▼
                            Model Selection
                         ┌────────┴────────┐
                         │                 │
                      Gemini             Claude
                         │            (OpenRouter)
                         └────────┬────────┘
                                  │
                                  ▼
                            LLM Router
                         (`ask_model()`)
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        Core AI Tools      Developer AI Tools   Data Science Tools
              │                   │                   │
              ├─ General Chat     ├─ Code Tools       ├─ Data Analysis
              ├─ Email Generator  ├─ SQL Tools        ├─ Data Science
              ├─ Resume Tools     ├─ Code Review      └─ Other AI Tools
              └─ Other AI Tools   └─ Developer Tools
                                  │
                                  ▼
                       Advanced LLM Features
                                  │
        ┌───────────────┬──────────────┬──────────────┬───────────────┐
        │               │              │              │               │
        ▼               ▼              ▼              ▼               ▼
   Research         Chat with      Document       Prompt         Document
   Assistant           PDF         Summarizer     Library           Q&A
                         │
                         ▼
                    RAG Pipeline
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
         PDF Loader            Text Splitter
              │                     │
              └──────────┬──────────┘
                         ▼
                   Embeddings
                         │
                         ▼
                  FAISS Vector Store
                         │
                         ▼
                  Semantic Search
                         │
                         ▼
                 Relevant Context
                         │
                         ▼
                    LLM Response

📁 Project Structure
text
Multi-LLM-AI-Workspace/
├── llms/               # LLM integrations and model routing   
├── menus/              # Menu / feature navigation            
├── tools/              # AI tools (developer, data science, etc.) 
├── ui/                 # User interface components            
├── utils/              # Helper functions                     
├── app.py              # Main application entry point         
├── streamlit_app.py    # Streamlit web interface
├── Run_MultiLLM.bat    # Quick-start script for Windows
├── requirements.txt    # Python dependencies
├── test_claude.py      # Tests: Claude integration
├── test_models.py      # Tests: model routing
├── test_pdf.py         # Tests: PDF processing
└── test_export.py      # Tests: export feature

⚙️ Installation and Setup
Prerequisites
Python 3.9 or higher [VERIFY]
A Google Gemini API key
An OpenRouter API key (for Claude)

**Steps**

# 1. Clone the repository
git clone https://github.com/sakshi-tongale/Multi-LLM-AI-Workspace.git
cd Multi-LLM-AI-Workspace

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

**Configuration**
Create a .env file in the project root and add your keys:

GEMINI_API_KEY=your_gemini_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

**▶️ Usage**

Run the Streamlit app:
streamlit run streamlit_app.py
**Or on Windows, double-click:**
Run_MultiLLM.bat

**Basic flow:**

Select a model (Gemini or Claude)
Choose a tool (Chat, Research Assistant, PDF Chat, Summarizer, etc.)
For PDF Chat, upload a document and ask questions about it
Export or reuse results as needed

🔮 Future Improvements
Add support for more LLM providers and models
Support multiple document uploads and DOCX / TXT files in RAG
Add user authentication and saved chat history
Deploy the app online (Streamlit Community Cloud)
Add response comparison view to see multiple models side by side
