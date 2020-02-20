from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        data = request.POST
        return HttpResponse(data['brand_name'])
    return render(request, 'manufacturers_feed/index.html')
