from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Cart

def add(request):
    if request.method == 'POST':
        cloth_price = request.POST['cloth_price']
        cloth_imge = request.POST['cloth_imge']
        cloth_offer = request.POST['cloth_offer']
        cloth_size = request.POST['cloth_size']
        cloth_color = request.POST['cloth_color']


        obj = Cart(cloth_image=cloth_imge,cloth_color=cloth_color,cloth_size=cloth_size,cloth_offer=cloth_offer,cloth_price=cloth_price)
        obj.save();
        obj1 = Cart.objects.all()
        return render(request, 'carts.html',{'obj1':obj1})
    else:
        obj1 = Cart.objects.all()
        return render(request, 'carts.html', {'obj1': obj1})


def cart(request):
    
    obj = Cart.objects.all()
    return render(request,'cart.html')
