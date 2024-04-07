from django.db import models

from random import choice
from string import ascii_letters, digits

SHORT_URL_SIZE = 7
AVAILABLE_CHARS = ascii_letters + digits

# Create your models here.


class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def create_short_url(self):
        url = ''
        for i in range(SHORT_URL_SIZE):
            url += choice(AVAILABLE_CHARS)

        if Shortener.objects.filter(short_url=url).exists():
            self.create_short_url()

        self.short_url = url
            
