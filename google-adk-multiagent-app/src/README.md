# Google ADK Multi-Agent Application

This project is a multi-agent architecture application that utilizes the Google Agent Development Kit (ADK) and Google Cloud BigQuery for data processing and analysis. The application features a web UI built with Streamlit, allowing users to upload datasets and interact with various agents for insights and visualizations.

## Project Structure

```
google-adk-multiagent-app
├── agents
│   ├── __init__.py
│   ├── agent_a.py
│   └── agent_b.py
├── bigquery
│   ├── __init__.py
│   └── client.py
├── streamlit_app
│   ├── __init__.py
│   ├── ui.py
│   └── upload.py
├── data
│   └── README.md
├── requirements.txt
├── README.md
└── main.py
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd google-adk-multiagent-app
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**
   Create a `.env` file in the root directory and add the following environment variables:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=<path-to-your-service-account-json>
   BIGQUERY_DATASET=<your-bigquery-dataset-name>
   DEBUG=True
   STREAMLIT_PORT=8501
   VERTEX_PROJECT=<your-gcp-project-id>
   VERTEX_LOCATION=<your-gcp-region>
   GEMINI_MODEL=gemini-1.0-pro
   ```

## Usage

To run the application, execute the following command:
```bash
python main.py
```

This will start the Streamlit application, which can be accessed at `http://localhost:8501`.

## Agents Overview

- **DataIngestionAgent**: Handles data uploads and API fetching from sources like Kaggle and stock data.
- **FormatDetectionAgent**: Detects the file type and schema of uploaded datasets.
- **BigQueryLoaderAgent**: Responsible for loading data into Google BigQuery.

## Streamlit UI

The Streamlit UI includes:
- A drag-and-drop interface for uploading datasets.
- Input fields for API keys and other configurations.
- Sections for displaying insights, charts, and a chatbot-style interface for user queries.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.