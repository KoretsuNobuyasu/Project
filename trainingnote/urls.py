from django.urls import path
from . import views

app_name = 'trainingnote'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('comment/<int:trainingnote_pk>',views.CommentView.as_view(), name='comment'),
]
