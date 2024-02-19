# views.py

from django.shortcuts import render
from controller import CSVAnalyzer


def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        analysis_result = CSVAnalyzer.analyze_csv(csv_file)
        return render(request, 'result.html', {'analysis_result': analysis_result})

    return render(request, 'upload.html')
