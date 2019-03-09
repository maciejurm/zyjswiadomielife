from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def userprofile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile/detail.html',
                {'user': user})