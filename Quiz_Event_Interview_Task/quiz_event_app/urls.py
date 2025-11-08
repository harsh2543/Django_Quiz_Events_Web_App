from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_attempt, name='quiz_attempt'),
    path('result/<int:submission_id>/', views.result, name='result'),
    path('events/', views.events, name='events'),
]