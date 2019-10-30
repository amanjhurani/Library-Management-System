from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from .forms import *
# Create your views here.
class BookList(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = "bookObj"
    ordering = ['BookTitle']

class BookAddView(CreateView):
    model = Book
    form_class = BookAddForm
    template_name = 'Add.html'
    success_url = reverse_lazy('home')


# class BookIssueView(CreateView):
#     model = Issued
#     form_class = BookIssueForm
#     template_name = 'Issue.html'
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super(BookIssueView, self).get_context_data(**kwargs)
#         context['obj'] = Book.objects.filter(pk = self.kwargs['pk'])
#         return context


class BookIssueView(CreateView):
    model = Issued
    form_class = BookIssueForm
    template_name = 'Issue.html'
    success_url = reverse_lazy('home')


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Book.objects.filter(Q(BookTitle__icontains=srch) | Q(BookISBN__icontains=srch))

            if match:
                return render(request, 'index.html',{'sr':match})
            else:
                messages.error(request,'No result Found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'index.html')




# class BookIssueView(DetailView):
#     model = Book
#     template_name = 'Issue.html'
def index(request):
    return render(request,'index.html')