from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=36)
    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name,last_name=self.last_name)
    class Meta:
        ordering = ['last_name']


class Publisher(models.Model):
    name = models.CharField(max_length=36,
            unique=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=63)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=8,
            unique=True)
    publisher = models.ForeignKey(Publisher)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

