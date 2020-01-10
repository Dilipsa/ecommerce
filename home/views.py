from django.shortcuts import render,get_object_or_404
from .models import Home

# Create your views here.
def index(request):
    obj = Home.objects.all()
    return render(request, 'index.html', {'obj':obj})


def cart(request):
    obj = Home.objects.all()
    return render(request, 'cart.html', {'obj':obj})


def detail(request, pk):
    det = get_object_or_404(Home, pk=pk)
    return render(request, 'detail.html', {'det': det})
    print(det.pk)
