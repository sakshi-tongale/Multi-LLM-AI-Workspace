import streamlit as st


def set_tool(tool_name):
    st.session_state.selected_tool = tool_name


def sidebar():

    # Default Page
    if "selected_tool" not in st.session_state:
        st.session_state.selected_tool = "Home"

    with st.sidebar:

        st.title("🤖 Multi-LLM AI Workspace")

        st.divider()

        # ---------------- Model ---------------- #

        model = st.radio(
            "🤖 Select AI Model",
            ["Gemini", "Claude"],
            key="model"
        )

        st.divider()

        st.subheader("📂 Categories")

        # ---------------- Home ---------------- #

        if st.button("🏠 Home", use_container_width=True):
            set_tool("Home")

        # ======================================================
        # Core AI Tools
        # ======================================================

        with st.expander("💼 Core AI Tools"):

            if st.button("💬 General Chat", use_container_width=True):
                set_tool("General Chat")

            if st.button("📄 Resume Analyzer", use_container_width=True):
                set_tool("Resume Analyzer")

            if st.button("📊 ATS Score", use_container_width=True):
                set_tool("ATS Score")

            if st.button("✉️ Cover Letter Generator", use_container_width=True):
                set_tool("Cover Letter Generator")

            if st.button("📧 Email Generator", use_container_width=True):
                set_tool("Email Generator")

            if st.button("📝 Meeting Notes Generator", use_container_width=True):
                set_tool("Meeting Notes Generator")

        # ======================================================
        # Developer AI Tools
        # ======================================================

        with st.expander("👨‍💻 Developer AI Tools"):

            if st.button("💻 Code Generator", use_container_width=True):
                set_tool("Code Generator")

            if st.button("🐞 Bug Fixer", use_container_width=True):
                set_tool("Bug Fixer")

            if st.button("📖 Code Explainer", use_container_width=True):
                set_tool("Code Explainer")

            if st.button("✅ Code Reviewer", use_container_width=True):
                set_tool("Code Reviewer")

            if st.button("🗄️ SQL Generator", use_container_width=True):
                set_tool("SQL Generator")

        # ======================================================
        # Data Science AI Tools
        # ======================================================

        with st.expander("📊 Data Science AI Tools"):

            if st.button("📈 CSV Analyzer", use_container_width=True):
                set_tool("CSV Analyzer")

            if st.button("📊 Data Visualization", use_container_width=True):
                set_tool("Data Visualization")

            if st.button("📋 Dataset Summary", use_container_width=True):
                set_tool("Dataset Summary")

            if st.button("📑 EDA Report", use_container_width=True):
                set_tool("EDA Report")

            if st.button("🤖 ML Model Recommender", use_container_width=True):
                set_tool("ML Model Recommender")

        # ======================================================
        # Advanced LLM Features
        # ======================================================

        with st.expander("🚀 Advanced LLM Features"):

            if st.button("📚 Research Assistant", use_container_width=True):
                set_tool("Research Assistant")

            if st.button("📄 Chat with PDF", use_container_width=True):
                set_tool("Chat with PDF")

            if st.button("❓ Document Q&A", use_container_width=True):
                set_tool("Document Q&A")

            if st.button("📝 Document Summarizer", use_container_width=True):
                set_tool("Document Summarizer")

            if st.button("📖 Prompt Library", use_container_width=True):
                set_tool("Prompt Library")

    return model, st.session_state.selected_tool