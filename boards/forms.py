from django.forms import ModelForm
from .models import Board, Subject
from django import forms

class BoardForm(ModelForm):

    class Meta:
        model = Board
        fields = ['title', 'image', 'body']


class Subject(ModelForm):
    
    class Meta:
        model = Subject
        fields = ['title', 'body', 'board']

class SubmitEmbed(forms.Form):
    url = forms.URLField()
    board = forms.ModelChoiceField(label="Kategoria", queryset=Board.objects.all().order_by('title'), required=False)
