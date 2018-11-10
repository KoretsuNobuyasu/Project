from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import CommentCreateForm
from .models import TrainingNote,Comment



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


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(TrainingNote, pk=post_pk)
        comment.save()
        return redirect('trainingnote:detail', pk=post_pk)
