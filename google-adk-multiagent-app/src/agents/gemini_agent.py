from vertexai.generative_models import GenerativeModel
import pandas as pd

class GeminiEDAAgent:
    def __init__(self, model_name=None):
        from dotenv import load_dotenv
        import os
        load_dotenv()
        self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        self.model = GenerativeModel(self.model_name)

    def run(self, data: pd.DataFrame, prompt="Provide an EDA summary for this data:"):
        data_str = data.to_csv(index=False)
        full_prompt = f"{prompt}\n\n{data_str}"
        response = self.model.generate_content(full_prompt)
        return {"summary": response.text}
