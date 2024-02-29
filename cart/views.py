from django.shortcuts import render,redirect
from . models import Cart
from mainapp.models import Product
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    try:
        cartitem=Cart.objects.get(user=user,products=product)
        if cartitem.quantity<cartitem.products.stock:
            cartitem.quantity+=1
            cartitem.price=cartitem.products.price*cartitem.quantity
            cartitem.save()
            
    except ObjectDoesNotExist:
            cartitem=Cart.objects.create(user=user,products=product,quantity=1,price=product.price)
            cartitem.save()
    return redirect('cart:displaycart')

def displaycart(req):
    totalprice=0
    user=req.session['user']
    cart=Cart.objects.all().filter(user=user)
    for i in cart:
        totalprice= totalprice+i.price
    
    
    return render(req,'cart.html',{"cart":cart,"totalprice":totalprice})

def remove(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cartitem=Cart.objects.get(user=user,products=product)
    if cartitem.quantity>1:
        cartitem.quantity-=1
        cartitem.price=cartitem.products.price*cartitem.quantity
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cart:displaycart')
def delete(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(user=user,products=product)
    cart.delete()
    return redirect('cart:displaycart')