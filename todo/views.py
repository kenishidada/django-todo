from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel
    

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('__all__')
    success_url = reverse_lazy('list')
    
    
class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = TodoModel
    success_url = reverse_lazy('list')
    

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo')
    # success_url = reverse_lazy('detail/<int:pk>')
    def get_success_url(self):
        return reverse_lazy("detail", kwargs={'pk': self.object.pk})
