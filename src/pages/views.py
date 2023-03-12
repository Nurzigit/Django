from django.shortcuts import render
from account.models import Account
from pages.forms import AddPostForm
from pages.models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
# Create your views here.

class IndexHome(ListView):
    model = Account
    template_name = 'pages/home.html'
    context_object_name = 'accounts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

# def home_screen_view(request):
#         context = {}
#         accounts = Account.object.all()
#         context['accounts'] = accounts;
        
#         return render(request, 'pages/home.html', context)

def about_screen_view(request):
        context = {}
        return render(request, 'pages/about.html', context)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'pages/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context
    
class ShowPost(DetailView):
    model = Post
    template_name = 'pages/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context

# ERRORS LOGIC
def error_404(request, exception):

        return render(request,'errors/404.html')

def error500(request, *args, **argv):
    return render(request, 'errors/500.html')
          
def error_403(request, exception):

        return render(request,'errors/403.html')

def error_400(request,  exception):
        data = {}
        return render(request,'errors/400.html', data) 