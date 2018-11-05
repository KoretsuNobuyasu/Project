from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Message, Menu, TrainingNote ,Category, Comment, Message_comment, ExpeditionReport
from .forms import CommentCreateForm, Message_commentCreateForm

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
    sucusess_url = reverse_lazy("homepage:index")
    permission_required = ("homepage.add_trainingnote", "homepage.change_trainingnote")

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = TrainingNote.objects.order_by('-created_at').filter(category=category)
        return queryset

class ExpeditionReportView(generic.ListView):
    model = ExpeditionReport
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = ExpeditionReport.objects.order_by('-created_at').filter(category=category)
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

class Message_detailView(generic.DetailView):
    model = Message


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        trainingnote_pk = self.kwargs['trainingnote_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(TrainingNote, pk=trainingnote_pk)
        comment.save()
        return redirect('homepage:detail', pk=trainingnote_pk)



class Message_CommentView(generic.ListView):
    model = Message_comment
    #form_class = Message_commentCreateForm
    """
    def form_valid(self, form):
        message_pk = self.kwargs['message_pk']
        message_comment = form.save(commit=False)
        message_comment.post = get_object_or_404(Message, pk=message_pk)
        message_comment.save()
        return redirect('homepage:message', pk=message_pk)
    """