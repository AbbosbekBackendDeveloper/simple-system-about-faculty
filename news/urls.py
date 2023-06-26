from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('news-list/', views.newslistview, name="news_list"),
    path('news-single/<slug:news>/', views.newsdetailview, name="news_detail"),
    path('news-search/', views.newssearchview, name="news_search"),
    path('our-contact/', views.contactview, name="contact"),
]