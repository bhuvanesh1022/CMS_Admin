from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('open_login', views.open_login, name='open_login'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('cms', views.cms, name='adminCMS'),
    path('add_decision', views.add_decision, name='add_decision'),
    path('load_decision', views.load_decision, name='load_decision'),
    path('show_decision', views.show_decision, name='show_decision'),
]