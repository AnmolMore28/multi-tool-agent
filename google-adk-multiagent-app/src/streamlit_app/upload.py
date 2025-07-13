from bigquery.client import BigQueryLoaderAgent
from agents.gemini_agent import GeminiEDAAgent
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    st.title("Data Upload, Analysis, and Prediction (Gemini + Visuals)")
    uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx", "json"])

    if uploaded_file is not None:
        # Read the file and display its contents
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            data = pd.read_json(uploaded_file)
        else:
            st.warning("Unsupported file type.")
            return
        st.write("Data Preview:")
        st.dataframe(data)

        # Gemini EDA summary
        gemini_agent = GeminiEDAAgent()
        with st.spinner("Gemini is analyzing your data..."):
            eda_result = gemini_agent.run(data)
        st.write("Gemini EDA Summary:", eda_result["summary"])

        # Optional: Visualizations
        if st.checkbox("Show Visualizations"):
            st.subheader("Feature Distributions")
            for col in data.select_dtypes(include='number').columns:
                fig = px.histogram(data, x=col)
                st.plotly_chart(fig)

        # Optional: Prediction
        if st.checkbox("Run Prediction (classification)"):
            target = st.selectbox("Select target column", data.columns)
            if st.button("Train Model"):
                X = data.drop(columns=[target])
                y = data[target]
                X = X.select_dtypes(include='number')
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model = RandomForestClassifier()
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)
                acc = accuracy_score(y_test, y_pred)
                st.write("Model accuracy:", acc)

        # Optionally, load data into BigQuery
        bigquery_loader_agent = BigQueryLoaderAgent()
        if st.button("Load Data to BigQuery"):
            try:
                table_name = uploaded_file.name.split('.')[0]
                rows = bigquery_loader_agent.load_data(table_name, data)
                st.success(f"Data loaded to BigQuery successfully! Rows: {rows}")
            except Exception as e:
                st.error(f"BigQuery load failed: {e}")

if __name__ == "__main__":
    main()