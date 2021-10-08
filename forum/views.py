from django.shortcuts import render, redirect
from .models import *
from .froms import *
from django.views.generic import ListView, DetailView

def addquestion(request):
    form= QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request,'forum/AddaQuestion.html', context)


class QuestionList(ListView):
    model= Question
    template_name = 'forum/QuestionList.html'
    context_object_name = 'questions'

class QestionDetail(DetailView):
    model = Question
    template_name = 'forum/QuestionDetail.html'
    context_object_name = 'questions'
    form_class= ResponseForm

    def get_context_data(self, **kwargs):
        context = super(QestionDetail, self).get_context_data(**kwargs)
        context['Responses'] = Response.objects.all()
        context['form'] = ResponseForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
