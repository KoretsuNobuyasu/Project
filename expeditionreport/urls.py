from django.urls import path
from . import views

app_name = 'expeditionreport'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('submission/', views.SubmissionView.as_view(), name='submission'),
]