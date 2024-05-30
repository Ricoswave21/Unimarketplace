from django.urls import path

from . import views

app_name = 'items'

urlpatterns = [
    path('new/',views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.Edit, name='edit'),
    path('<int:pk>/contact-seller/', views.contact_seller, name='contact_seller'),

]