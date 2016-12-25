from django.shortcuts import render


def index(request):
    return render(request, 'hptrivia_app/base.html')
