from django.shortcuts import render
from mainapp.models import Product
from django.db.models import Q
# Create your views here.
def search(req):
    product=None
    query=None
    if 'q' in req.GET:
        query=req.GET.get('q')
    product=Product.objects.all().filter(Q(name__contains=query))
    return render(req,'search.html',{"product":product})
