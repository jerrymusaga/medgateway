from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post, Question
from comments.models import Comment



class PostIndexView(ListView):
    model = Post
    template_name = 'project/index.html'

class PostHomeView(ListView):
    model = Post
    template_name = 'project/home.html'
    context_object_name = 'post'
    ordering = ['-date_published']

    #user = get_object_or_404(Post)
    #content_type = ContentType.objects.get_for_model(Post)
    #obj_id = user.id
    #comments = Comment.objects.filter(content_type=content_type, object_id=obj_id)

class QuestionHomeView(ListView):
    model = Question
    template_name = 'project/home_question.html'
    context_object_name = 'question'
    ordering = ['-date_published']

class UserPostHomeView(ListView):
    model = Post
    template_name = 'project/user_posts.html'
    context_object_name = 'post'
    

    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_published')


class UserQuestionHomeView(ListView):
    model = Question
    template_name = 'project/user_questions.html'
    context_object_name = 'question'
    

    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Question.objects.filter(author=user).order_by('-date_published')



class PostDetailView(DetailView):
    model = Post

class QuestionDetailView(DetailView):
    model = Question
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['topic','content']

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question']

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['topic','content']

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question']

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/post'    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/question'    

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False





