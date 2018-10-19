from django.views import generic
from .models import Message, Category, TrainingNote

class IndexView(generic.ListView):
    model = Message

    def get_queryset(self):
        return Message.objects.order_by('-created_at')