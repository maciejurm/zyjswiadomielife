from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from actstream import action
from autoslug import AutoSlugField
from django.urls import reverse
from django.utils import timezone


class Board(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    slug = AutoSlugField(populate_from='title', unique=True)
    image = models.ImageField(upload_to='board-cover', verbose_name='Tło kategorii', null=True, blank=True)
    body = models.TextField(verbose_name='Opis kategorii')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name='Dział'

    def get_absolute_url(self):
        return reverse('board',
                        args=[self.slug])

    def add_user_to_list_of_subscribers(self, user):
        registration = Subscribe.objects.create(user = user,
                                                    board = self,
                                                    created_at = timezone.now())

    def remove_user_from_list_of_subscribers(self, user):
        registration = Subscribe.objects.get(user = user, board = self)
        registration.delete()

class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribed_users')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='subscribed_boards')
    created_at = models.DateTimeField(auto_now_add=True)
    subscribe = models.BooleanField(default=False)

    def __str__(self):
        return 'Użytkownik {} zaczął obserwować {}'.format(self.user, self.board)

    def save(self, *args, **kwargs):
        if self.id is None and self.created_at is None:
            self.created_at = datetime.datetime.now()
        self.subscribe = True
        super(Subscribe, self).save(*args, **kwargs)


class Subject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tytuł')
    slug = AutoSlugField(populate_from='title', unique=True)
    body = models.TextField(blank=True, verbose_name='Treść')
    image = models.ImageField(upload_to='subject', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='subjects', verbose_name='Kategoria')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'

    def get_absolute_url(self):
        return reverse('subject_detail',
                       args=[self.slug])

class Embed(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail_url = models.URLField(max_length=255)
    html = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('embeddetail',
                       args=[self.id])

    class Meta:
        ordering = ['-created_at']
