from .models import Category,Subcategory

def menu_links(req):
    links=Category.objects.all()
    return dict(category=links)


def sub_links(req):
    links=Subcategory.objects.all()
    return dict(subcategory=links)