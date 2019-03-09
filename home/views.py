from django.shortcuts import render
from boards.models import Board, Subject, Embed
from django.views.generic import ListView

class HomeList(ListView):
    model = Board

    def get_context_data(self, *args, **kwargs):
        context = super(HomeList, self).get_context_data(*args, **kwargs)

        context['subjects'] = Subject.objects.all()
        context['embeds'] = Embed.objects.all()
 
        return context