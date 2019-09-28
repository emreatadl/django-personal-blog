from django.db.models import Count, Q
from django.shortcuts import render


def analysis_index(request):
    return render(request, 'charts.html')