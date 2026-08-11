# Multi-LLM AI Workspace

A Python-based Generative AI application that integrates multiple Large Language Models, including Google Gemini and Claude through Open Router. The project provides a unified workspace for AI-powered productivity, developer, document, research, and data science workflows.

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
