from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Subject, Embed, Subscribe
from comments.forms import SubjectcommentForm, EmbedcommentForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import requests
import json

from .forms import SubmitEmbed
from .serializer import EmbedSerializer


def save_embed(request):
    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            board = form.cleaned_data['board']
            r = requests.get('http://iframe.ly/api/oembed?url='+ url + '&api_key=' + '493c9ebbdfcbdac2a10d6b')
            json = r.json()
            if board:
                json['board'] = board.id
            serializer = EmbedSerializer(data=json, context={'request': request})
            if serializer.is_valid():
                embed = serializer.save()
                return render(request, 'embed/embeds.html', {'embed': embed})
    else:
        form = SubmitEmbed()

    return render(request, 'embed/embedadd.html', {'form': form})


class BoardsPageView(ListView):
    """
    Basic ListView implementation to call the boards list.
    """
    model = Board
    queryset = Board.objects.all()
    paginate_by = 20
    template_name = 'boards/list.html'
    context_object_name = 'boards'


def boarddetail(request, slug):
    board = get_object_or_404(Board, slug=slug)
    subjects = board.subjects.all()

    return render(request, 'board/boarddetail.html', {'board': board,
                                                      'subjects': subjects})


class UserSubscriptionListView(ListView):
    model = Subscribe
    paginate_by = 10
    template_name = 'boards/user_subscription_list.html'
    context_object_name = 'subscriptions'

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User, username=self.request.user)
        return user.subscribed_users.all()


def feed(request):
    userids = []
    for id in request.user.subscribed_boards.all():
        userids.append(id)

    userids.append(request.user.id)
    subjects = Subject.objects.filter(board_id__in=userids)[0:25]
    embeds = Embed.objects.filter(board_id__in=userids)[0:25]

    return render(request, 'boards/feed.html', {'subjects': subjects,
                                                'embeds': embeds})


class BoardCreate(CreateView):
    model = Board
    fields = ['title', 'image', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def subjectlist(request):
    subjects = Subject.objects.all()
    return render(request, 'boards/subjectlist.html',
                            {'subjects': subjects})


def subjectdetail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)

    comments = subject.subjectcomments.all()

    if request.method == 'POST':
        form = SubjectcommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.subject = subject
            new_comment.save()
    else:
        form = SubjectcommentForm()

    return render(request,
        'board/subjectdetail.html',
        {'subject': subject,
        'comments': comments,
        'form': form})


class SubjectCreate(CreateView):

    model = Subject
    fields = ['title', 'embed', 'body', 'board']
    #  fields = ['title', 'body', 'board']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def embeddetail(request, id):
    embed = get_object_or_404(Embed, id=id)

    comments = embed.embedcomments.all()

    if request.method == 'POST':
        form = EmbedcommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.embed = embed
            new_comment.save()
    else:
        form = EmbedcommentForm()

    return render(request, 'embed/embed_detail.html',
                {'embed': embed,
                'form': form,
                'comments': comments})


def subscribe(request, board):
    """
    Subscribes a board & returns subscribers count.
    """
    board = get_object_or_404(Board,
                              slug=board)
    user = request.user
    if board in user.subscribed_boards.all():
        board.subscribers.remove(user)
    else:
        board.subscribers.add(user)
    return HttpResponse(board.subscribers.count())


def subscribe_add(request, pk):
    this_board = Board.objects.get(pk=pk)
    this_board.add_user_to_list_of_subscribers(user=request.user)
    return redirect('boardlist')


def subscribe_delete(request, pk):
    this_board = Board.objects.get(pk=pk)
    this_board.remove_user_from_list_of_subscribers(request.user)
    return redirect('boardlist')
