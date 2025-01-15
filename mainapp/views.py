from django.shortcuts import render,get_object_or_404,redirect
from . models import Category,Product,Subcategory,Ads
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(req):
    ads=Ads.objects.all()
 
    return render(req,'index.html',{"ads":ads})
def mproduct(req,id=None):
    c_page=None
    
    if id!=None:
        cat=Category.objects.get(pk=id)
        c_page=Subcategory.objects.filter(category=cat)
        l=[]
        for i in c_page:
           
            pro=Product.objects.filter(category=i)
            
            for j in pro:
                l.append(j)
       
    paginator=Paginator(l,16)
    try:
        page=int(req.GET.get('page'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(req,"catproducts.html",{"product":products,"cat":c_page})

def product(req,id=None,):
    c_page=None
    if id!=None:
        c_page=get_object_or_404(Subcategory,id=id,)
        product=Product.objects.all().filter(category_id=c_page,available=True)
        # cat=Category.objects.get(pk=id)
        
        # sub=Subcategory.objects.filter(category=cat)
        # print("t",sub)
        # l=[]
        # for i in sub:
        #     print('i',i)
        #     pro=Product.objects.filter(category=i)
        #     for j in pro:
        #         l.append(j)
        # print(l)
        
    else:
        product=Product.objects.all().filter(available=True)
        # cat=Category.objects.get(pk=id)
        
        # sub=Subcategory.objects.filter(category=cat)
        # print(sub)
        # pro=Product.objects.filter()
        
    paginator=Paginator(product,12)
    
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
    product=Product.objects.filter(category=details.category)
    return render(req,'details.html',{"details":details,"product":product})