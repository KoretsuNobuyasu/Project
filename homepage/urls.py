from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>/',views.CategoryView.as_view(),name='category'),
    path('menu/<int:pk>/',views.MenuView.as_view(),name='menu'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
]
