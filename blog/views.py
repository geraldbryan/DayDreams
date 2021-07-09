from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Sad, Anger

# Happiness Post
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Sadness Post

def sad(request):
    context = {
        'sad': Sad.objects.all()
    }
    return render(request, 'blog/sad.html', context)

class SadListView(ListView):
    model = Sad
    template_name = 'blog/sad.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'sad'
    ordering = ['-date_posted']
    paginate_by = 5

class SadCreateView(LoginRequiredMixin, CreateView):
    model = Sad
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Stressfull Post
def anger(request):
    context = {
        'anger': Anger.objects.all()
    }
    return render(request, 'blog/sad.html', context)

class AngerListView(ListView):
    model = Anger
    template_name = 'blog/anger.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'anger'
    ordering = ['-date_posted']
    paginate_by = 5

class AngerCreateView(LoginRequiredMixin, CreateView):
    model = Anger
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Not about post
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def landing(request):
    return render(request, 'blog/landing.html',{})

def menu(request):
    return render(request, 'blog/menu.html',{})