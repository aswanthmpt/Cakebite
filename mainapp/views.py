from django.shortcuts import render,get_object_or_404,redirect
from . models import Category,Product,Subcategory
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(req):
 
    return render(req,'index.html')

def product(req,id=None,):
    c_page=None
    if id!=None:
        c_page=get_object_or_404(Subcategory,id=id,)
        product=Product.objects.all().filter(category_id=c_page,available=True)
    else:
        product=Product.objects.all().filter(available=True)
    paginator=Paginator(product,16)
    
    try:
        page=int(req.GET.get('page'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    
   
    
    return render(req,'products.html',{"product":products,"cat":c_page})

def details(req,id):
    details=Product.objects.get(id=id)
    
    return render(req,'details.html',{"details":details})