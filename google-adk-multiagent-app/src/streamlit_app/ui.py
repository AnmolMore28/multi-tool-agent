import streamlit as st
import pandas as pd
from agents.gemini_agent import GeminiEDAAgent
from bigquery.client import BigQueryLoaderAgent
import os
from dotenv import load_dotenv

def run_app(bigquery_loader_agent=None):
    load_dotenv()
    st.title("Data Upload and Analysis (Multi-file)")

    st.sidebar.header("Upload Data")
    uploaded_files = st.sidebar.file_uploader("Choose files", type=["csv", "xlsx", "json"], accept_multiple_files=True)

    st.sidebar.header("API Key")
    api_key = st.sidebar.text_input("Enter your API Key", type="password")
    if st.sidebar.button("Submit API Key"):
        st.sidebar.success("API Key submitted!")

    st.header("Insights and Analysis (Powered by Gemini)")
    if uploaded_files:
        gemini_agent = GeminiEDAAgent()
        for uploaded_file in uploaded_files:
            st.subheader(f"File: {uploaded_file.name}")
            # Read file
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                data = pd.read_excel(uploaded_file)
            elif uploaded_file.name.endswith('.json'):
                data = pd.read_json(uploaded_file)
            else:
                st.warning("Unsupported file type.")
                continue
            st.write("Data Preview:")
            st.dataframe(data)

            # Use Gemini LLM for EDA/Summary
            with st.spinner("Gemini is analyzing your data..."):
                eda_result = gemini_agent.run(data)
            st.write("Gemini EDA Summary:", eda_result["summary"])

            # Optionally, load to BigQuery
            if st.button(f"Load {uploaded_file.name} to BigQuery"):
                if bigquery_loader_agent:
                    table_name = os.path.splitext(uploaded_file.name)[0]
                    try:
                        rows = bigquery_loader_agent.load_data(table_name, data)
                        st.success(f"Loaded {rows} rows to BigQuery table {table_name}!")
                    except Exception as e:
                        st.error(f"BigQuery load failed: {e}")
                else:
                    st.warning("BigQuery agent not initialized.")

    st.header("Chatbot Queries (Powered by Gemini)")
    user_query = st.text_input("Ask a question about your data:")
    if st.button("Submit Query"):
        if uploaded_files:
            # Use the first file's data for context
            data = None
            if uploaded_files[0].name.endswith('.csv'):
                data = pd.read_csv(uploaded_files[0])
            elif uploaded_files[0].name.endswith('.xlsx'):
                data = pd.read_excel(uploaded_files[0])
            elif uploaded_files[0].name.endswith('.json'):
                data = pd.read_json(uploaded_files[0])
            if data is not None:
                gemini_agent = GeminiEDAAgent()
                prompt = f"Answer this question about the data: {user_query}"
                result = gemini_agent.run(data, prompt=prompt)
                st.success(result["summary"])
            else:
                st.warning("No valid data to answer the query.")
        else:
            st.warning("Please upload a file first.")

def main():
    # Backward compatibility for direct run
    run_app(None)

if __name__ == "__main__":
    main()