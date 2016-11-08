from django.contrib import admin
from .models import Author, Publisher, Book

# Register your models here.

# Rejestracja klasy administrujacej - bez opcji
#class AuthorAdmin(admin.ModelAdmin):
#    pass

# to samo + wyszukiwarka wybranych pol modelu
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    ordering = ['last_name']

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'publisher', 'isbn']
    ordering = ['title']

# Rejestracja modelu za pomoca klasy administrujacej. Pierwszy musi byc model, dopiero po nim klasa administurjaca
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
# LUB
# Rejestrowanie modeli za pomoca listy elementow(modeli)
#admin.site.register([Author,Publisher, Book])
admin.site.register([Publisher])

