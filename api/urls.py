from django.urls import path
from api import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', view = views.index, name='index'),
    path('<str:image>/', views.searchImage.as_view(), name='search_image'),
]