from django import forms
from .models import *

class QuestionForm(forms.ModelForm):

    class Meta:
        model= Question
        fields = ['subject','description','user']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'
