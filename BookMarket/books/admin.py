from django.contrib import admin
from books.models import Book,Comment,Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthDate', 'age')  # age alanını listeye ekledik



admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Author, AuthorAdmin)