from django.urls import path
from .views import (PostIndexView, PostHomeView, UserPostHomeView, PostDetailView, PostCreateView,
 PostUpdateView,
 PostDeleteView, 
 QuestionCreateView,
 QuestionUpdateView,
 QuestionDetailView,
 QuestionDeleteView,
 UserQuestionHomeView,
 QuestionHomeView,)

urlpatterns = [
    path('',PostIndexView.as_view(),name='index'),
    path('post/',PostHomeView.as_view(),name='home'),
    path('question/',QuestionHomeView.as_view(),name='home_question'),
    path('user/<str:username>/',UserPostHomeView.as_view(),name='user_posts'),
    path('user/<str:username>/',UserQuestionHomeView.as_view(),name='user_questions'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='detail'),
    path('question/<int:pk>/', QuestionDetailView.as_view(),name='question_detail'),
    path('post/create/', PostCreateView.as_view(),name='create'),
    path('question/create/', QuestionCreateView.as_view(),name='create_question'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='update'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(),name='update_question'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='delete'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(),name='delete_question'),
    
]