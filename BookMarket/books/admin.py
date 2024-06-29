from django.contrib import admin
from books.models import Book,Comment,Author
# Register your models here.

class BookInline(admin.StackedInline):  # or admin.TabularInline for a tabular view
    model = Book
    extra = 0  # Controls the number of empty forms to display

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthDate', 'age', 'display_books')  # Include 'display_books' in list_display
    inlines = [BookInline]  # Include the BookInline to display books inline with authors

    def display_books(self, obj):
        return ", ".join([book.name for book in obj.books.all()])

    display_books.short_description = 'Books'  # Set the column header name




class BookAdmin(admin.ModelAdmin):
    list_display= ('name','author','published_date')
    search_fields= ('name',)
    
    
admin.site.register(Book,BookAdmin)
admin.site.register(Comment)
admin.site.register(Author, AuthorAdmin)