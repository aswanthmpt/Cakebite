from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('addcart  /<int:id>',views.addcart,name='addcart'),
    path('displaycart/',views.displaycart,name='displaycart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('delete/<int:id>',views.delete,name='delete'),
    
]
