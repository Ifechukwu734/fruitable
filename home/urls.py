from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('signup/', views.signup, name='sign_up'),
    path('signup/verify/', views.verify, name='verify')
]