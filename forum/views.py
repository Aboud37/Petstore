from django.shortcuts import render, redirect
from .models import *
from .froms import *
from django.views.generic import ListView, DetailView

def addquestion(request):
    form= QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'forum/AddaQuestion.html', context)


class QuestionList(ListView):
    model= Question
    template_name = 'forum/QuestionList.html'
    context_object_name = 'questions'