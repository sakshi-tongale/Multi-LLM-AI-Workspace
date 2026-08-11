@echo off
cd /d C:\Users\Admin\Multi-LLM-AI-Workspace

call venv\Scripts\activate

python -m streamlit run streamlit_app.py --server.port 8502

pause