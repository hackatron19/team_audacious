from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'index.html'
    context_object_name = "blog_entries"
    ordering = ['entry_date']
    paginate_by = 3


class EntryView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'create_entry.html'
    fields = ['entry_title', 'entry_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)



