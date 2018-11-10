from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Post, Menu, Comment
from .forms import CommentCreateForm

class IndexView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(text__icontains=keyword) | Q(news__icontains=keyword)
            )
        return queryset

class MenuView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        menu = get_object_or_404(Menu, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(menu=menu)
        return queryset


class DetailView(generic.DetailView):
    model = Post


class CommentView(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=post_pk)
        comment.save()
        return redirect('homepage:detail', pk=post_pk)
