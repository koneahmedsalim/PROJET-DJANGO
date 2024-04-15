from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='dashboard'),
    path('customers/', views.customers,name='customers'),
    path('products/', views.products,name='products'),
    path('about/', views.about,name='about'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]
