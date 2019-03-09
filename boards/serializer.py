from rest_framework import serializers
from .models import Embed
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
     class Meta:
         model = Board
         fields = ('title')

class EmbedSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    board = BoardSerializer(read_only=False)

    class Meta:
        model = Embed
        fields = '__all__'

