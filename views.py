"""
views.py - Django views for CSV analysis application.

This module contains views for handling file uploads, performing CSV analysis,
and rendering result pages.

Author: Ryan Zimmerly
Date: February 18, 2024
"""

from django.shortcuts import render
from controller import CSVAnalyzer


def upload_csv(request):
    """
    Handles file upload and renders the result page.

    If a file is provided via a POST request, analyzes the CSV file using CSVAnalyzer
    and renders the result page. Otherwise, renders the upload form.

    :param request: Django HttpRequest object
    :return: Rendered HTML page with analysis result or upload form
    """
    if request.method == 'POST' and request.FILES['file']:
        # Analyze the CSV file using CSVAnalyzer if a file is provided
        csv_file = request.FILES['file']
        result = CSVAnalyzer.analyze_csv(csv_file)
        return render(request, 'result.html', {'result': result})

    # Render the upload form for GET requests or when no file is provided
    return render(request, 'upload.html')
