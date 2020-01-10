from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('otp/', views.otp, name='otp'),
    path('thanku/', views.thanku, name='thanku'),
    path('cart/', views.cart, name='cart'),

]
