from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view),
    path('<str:slug>', views.read_article),
    #path('',views.home_view, name="home"),
]
