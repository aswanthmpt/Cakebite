from django.urls import path
from . import views
app_name='user'
urlpatterns = [
    path('login/',views.login_u,name='login'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout_u,name='logout'),
    path('forpass/',views.forgotpass,name='forpass'),
    path('password_reset_otp/',views.password_reset_otp,name='password_reset_otp'),
    path('password_reset_form/',views.password_reset_form,name='password_reset_form'),
]
