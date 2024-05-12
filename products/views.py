from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
# Create your views here.

# class ListView(View):
#     def get(self, request):
#         book = Books.objects.all().order_by('-id')
#         return render(request, 'book_list.html', {'book': book})

class BookListView(ListView):
    model = Books
    template_name = 'book/book_list.html'
    context_object_name = 'book'


class BookDetailView(DetailView):
    model = Books.objects.get(pk=pk)
    template_name = 'book/book_detail.html'
