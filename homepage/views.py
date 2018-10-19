from django.views import generic
from .models import Message, Category, TrainingNote

class IndexView(generic.ListView):
    model = Message