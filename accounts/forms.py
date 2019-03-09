from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileEditForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['photo', 'bio', 'facebook', 'www']