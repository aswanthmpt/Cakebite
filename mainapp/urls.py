from django.urls import path
from . import views
app_name='main'
urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:id>',views.details,name='details'),
    path('product/',views.product,name='product'),
    path('prod_by_cat/<int:id>',views.product,name='prod_by_cat'),
]
