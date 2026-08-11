import streamlit as st

from ui.sidebar import sidebar
from ui.home import home_page

# ================= CORE ================= #

from ui.core.general_chat import general_chat_page
from ui.core.resume_analyzer import resume_analyzer_page
from ui.core.ats_score import ats_score_page
from ui.core.cover_letter_generator import cover_letter_generator_page
from ui.core.email_generator import email_generator_page
from ui.core.meeting_notes_generator import meeting_notes_generator_page

# ================= DEVELOPER ================= #

from ui.developer.python_code_generator import python_code_generator_page
from ui.developer.bug_fixer import bug_fixer_page
from ui.developer.code_explainer import code_explainer_page
from ui.developer.code_reviewer import code_reviewer_page
from ui.developer.sql_query_generator import sql_query_generator_page

# ================= DATA SCIENCE ================= #

from ui.data_science.csv_data_analyzer import csv_data_analyzer_page
from ui.data_science.data_visualization_assistant import (
    data_visualization_assistant_page,
)
from ui.data_science.dataset_summary_generator import (
    dataset_summary_generator_page,
)
from ui.data_science.eda_report_generator import eda_report_generator_page
from ui.data_science.ml_model_recommender import (
    ml_model_recommender_page,
)

# ================= ADVANCED ================= #

from ui.advanced.ai_research_assistant import research_assistant_page
from ui.advanced.chat_with_pdf import chat_with_pdf_page
from ui.advanced.document_question_answer import document_qa_page
from ui.advanced.document_summary import (
    document_summarizer_page,
)
from ui.advanced.ai_prompt_library import prompt_library_page


# ==================================================

st.set_page_config(
    page_title="Multi-LLM AI Workspace",
    page_icon="🤖",
    layout="wide",
)

# Sidebar
model, tool = sidebar()

# ================= ROUTER ================= #

if tool == "Home":
    home_page()

# ================= CORE ================= #

elif tool == "General Chat":
    general_chat_page(model)

elif tool == "Resume Analyzer":
    resume_analyzer_page(model)

elif tool == "ATS Score":
    ats_score_page(model)

elif tool == "Cover Letter Generator":
    cover_letter_generator_page(model)

elif tool == "Email Generator":
    email_generator_page(model)

elif tool == "Meeting Notes Generator":
    meeting_notes_generator_page(model)

# ================= DEVELOPER ================= #

elif tool == "Code Generator":
    python_code_generator_page(model)

elif tool == "Bug Fixer":
    bug_fixer_page(model)

elif tool == "Code Explainer":
    code_explainer_page(model)

elif tool == "Code Reviewer":
    code_reviewer_page(model)

elif tool == "SQL Generator":
    sql_query_generator_page(model)

# ================= DATA SCIENCE ================= #

elif tool == "CSV Analyzer":
    csv_data_analyzer_page(model)

elif tool == "Data Visualization":
    data_visualization_assistant_page(model)

elif tool == "Dataset Summary":
    dataset_summary_generator_page(model)

elif tool == "EDA Report":
    eda_report_generator_page(model)

elif tool == "ML Model Recommender":
    ml_model_recommender_page(model)

# ================= ADVANCED ================= #

elif tool == "Research Assistant":
    research_assistant_page(model)

elif tool == "Chat with PDF":
    chat_with_pdf_page(model)

elif tool == "Document Q&A":
    document_qa_page(model)

elif tool == "Document Summarizer":
    document_summarizer_page(model)

elif tool == "Prompt Library":
    prompt_library_page(model)

# ================= UNKNOWN ================= #

else:
    st.title("❌ Page Not Found")
    st.error(f"No page found for '{tool}'.")