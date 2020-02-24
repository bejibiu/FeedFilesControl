from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        data = request.POST
        return render(request, 'manufacturers_feed/index.html', {'brand_name': data['brand_name']})
    return render(request, 'manufacturers_feed/index.html')
