from django.urls import path
from . import views


urlpatterns = [
    path('', views.process_payments, name='process'),
    path('payment_done/', views.payment_done, name='payment_done'),
    path('payment_cancelled/', views.payment_cancelled, name='payment_cancelled')
]