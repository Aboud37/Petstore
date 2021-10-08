from django import forms
from .models import *

class QuestionForm(forms.ModelForm):

    class Meta:
        model= Question
        fields = ['subject','name','description']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['name','description']
