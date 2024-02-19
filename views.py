# views.py

from django.shortcuts import render
from controller import CSVAnalyzer


def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        result = CSVAnalyzer.analyze_csv(csv_file)
        return render(request, 'result.html', {'result': result})

    return render(request, 'upload.html')
