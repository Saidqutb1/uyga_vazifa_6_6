from django.contrib import admin
from .models import Review, Books, Author, CategoryBook, BookAuthor, Language
# Register your models here.

admin.site.register(Author)
admin.site.register(CategoryBook)
admin.site.register(Books)
admin.site.register(BookAuthor)
admin.site.register(Review)
admin.site.register(Language)