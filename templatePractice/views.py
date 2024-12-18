from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def portfolio(request):
    context = {'number_of_photos': 3}
    return render(request, 'bestphotos.html', context)
