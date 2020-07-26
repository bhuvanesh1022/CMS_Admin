from django.urls import path
from . import views

urlpatterns = [
    path('', views.cms, name='adminCMS'),
    # path('adminCMS', views.cms, name='adminCMS'),
]