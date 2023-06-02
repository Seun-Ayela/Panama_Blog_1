from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('Homepage')

# def room(request):
#     return HttpResponse('Room')

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')

def footer(request):
    return render(request, 'footer.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

def summary(request):
    return render(request, 'summary.html')

def base(request):
    return render(request, 'base.html')

def header(request):
    return render(request, 'header.html')
