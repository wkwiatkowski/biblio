from django.shortcuts import render

#zaimportowanie widokow generycznych
from django.views.generic import ListView, DetailView

#zaimportowanie obiektu z submodulu
from .models import Author, Book, Publisher

# Create your views here.

#Tworzenie klasy
class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class BookListView(ListView):
    model = Book

class PublisherListView(ListView):
    model = Publisher


