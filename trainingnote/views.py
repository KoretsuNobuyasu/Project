from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import CommentCreateForm, TrainingnoteCreateForm
from .models import TrainingNote,Comment
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(generic.ListView):
    model = TrainingNote
    paginate_by = 10

    def get_queryset(self):
        queryset = TrainingNote.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(text__icontains=keyword) | Q(news__icontains=keyword)
            )
        return queryset


class DetailView(generic.DetailView):
    model = TrainingNote


class CommentView(LoginRequiredMixin,generic.CreateView):
    login_url = '/admin'
    redirect_field_name = 'redirect_to'
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        trainingnote_pk = self.kwargs['trainingnote_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(TrainingNote, pk=trainingnote_pk)
        comment.save()
        return redirect('trainingnote:detail', pk=trainingnote_pk)


class SubmissionView(LoginRequiredMixin,generic.CreateView):
    login_url = '/admin'
    redirect_field_name = 'redirect_to'
    model = TrainingNote
    form_class = TrainingnoteCreateForm

    def form_valid(self, form):
        self.object = None
        note = form.save(commit=False)
        #note.post = get_object_or_404(TrainingNote)
        note.save()
        return redirect('trainingnote:index')
