from django.db import models
from django.urls import reverse


class Phones(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    brand = models.ForeignKey('Brands', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Brands(models.Model):
    name = models.CharField(max_length=15, db_index=True)

    def __str__(self):
        return self.name