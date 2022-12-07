from django.shortcuts import render


def homePage(request):
    # home page
    return render(request, 'index.html')
