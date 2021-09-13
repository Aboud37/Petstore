from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('ajouter_une_question', views.addquestion, name='ajouter_une_question'),
    path('questions', QuestionList.as_view(), name='questions'),
]
