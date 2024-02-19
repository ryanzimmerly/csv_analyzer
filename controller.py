# controller.py

import pandas as pd


class CSVAnalyzer:
    @staticmethod
    def analyze_csv(file):
        try:
            df = pd.read_csv(file)
            return df.describe()
        except Exception as e:
            return f"Error analyzing CSV file: {e}"
