from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Expeditionreport
from .forms import ExpeditionreportCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    model = Expeditionreport
    paginate_by = 10

    def get_queryset(self):
        queryset = Expeditionreport.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(text__icontains=keyword) | Q(news__icontains=keyword)
            )
        return queryset

class DetailView(generic.DetailView):
    model = Expeditionreport


class SubmissionView(generic.CreateView):
    model = Expeditionreport
    form_class = ExpeditionreportCreateForm

    def form_valid(self, form):
        self.object = None
        note = form.save(commit=False)
        #note.post = get_object_or_404(TrainingNote)
        note.save()
        return redirect('expeditionreport:index')