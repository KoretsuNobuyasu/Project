from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Message, Menu, TrainingNote ,Category

class IndexView(generic.ListView):
    model = Message
    paginate_by = 10

    def get_queryset(self):
        queryset = Message.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(text__icontains=keyword) | Q(news__icontains=keyword)
            )
        return queryset


class CategoryView(generic.ListView):
    model = TrainingNote
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = TrainingNote.objects.order_by('-created_at').filter(category=category)
        return queryset


class MenuView(generic.ListView):
    model = Message
    paginate_by = 10

    def get_queryset(self):
        menu = get_object_or_404(Menu, pk=self.kwargs['pk'])
        queryset = Message.objects.order_by('-created_at').filter(menu=menu)
        return queryset


class DetailView(generic.DetailView):
    model = TrainingNote