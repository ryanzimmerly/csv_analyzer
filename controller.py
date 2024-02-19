"""
controller.py - CSVAnalyzer class for analyzing CSV files.

This module contains the CSVAnalyzer class, which provides methods for analyzing
CSV files, such as reading a CSV file and generating a statistical summary.

Author: Ryan Zimmerly
Date: February 18, 2024
"""

import pandas as pd


class CSVAnalyzer:
    @staticmethod
    def analyze_csv(file):
        """
        Analyzes a CSV file and returns a statistical summary.

        This static method reads the provided CSV file using the pandas library
        and generates a statistical summary using the describe() function.

        :param file: File-like object or path-like object representing the CSV file.
        :return: Pandas DataFrame containing the statistical summary or an error message.
        """
        try:
            df = pd.read_csv(file)
            return df.describe()
        except Exception as e:
            return f"Error analyzing CSV file: {e}"
