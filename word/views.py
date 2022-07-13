from django.shortcuts import render


# Create your views here.
def say_hi(request):
    return render(request, 'index.html', {'name': 'MAMF'})
