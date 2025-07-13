class BigQueryLoaderAgent:
    def __init__(self, dataset_name, credentials_path):
        from google.cloud import bigquery
        self.client = bigquery.Client.from_service_account_json(credentials_path)
        self.dataset_name = dataset_name

    def load_data(self, table_name, dataframe):
        table_id = f"{self.client.project}.{self.dataset_name}.{table_name}"
        job = self.client.load_table_from_dataframe(dataframe, table_id)
        job.result()  # Wait for the job to complete.
        return job.output_rows

    def query_data(self, query):
        query_job = self.client.query(query)
        return query_job.result().to_dataframe()