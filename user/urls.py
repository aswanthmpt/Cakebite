from django.urls import path
from . import views
app_name='user'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
]
