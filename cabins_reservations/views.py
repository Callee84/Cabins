from django.shortcuts import render

# Create your views here.


def cabinOland(request):
    return render(request, 'cabin_oland.html')


def cabinSalen(request):
    return render(request, 'cabin_salen.html')
