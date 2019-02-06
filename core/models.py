from django.contrib.auth.models import User
from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def dictionary_directory_path(instance, filename):
    return '/dictionary_{}/avatar/{}'.format(instance.pk, filename)


class Dictionary(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dictionaries')
    title = models.CharField(max_length=256)
    avatar = models.ImageField(upload_to=dictionary_directory_path, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'dictionaries'

    def __str__(self):
        return self.title


class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='words')
    word = models.CharField(max_length=256)
    definition = models.TextField()

    def __str__(self):
        return self.word
