from django.contrib import admin
from .models import Book, Member, BarrowedBook, User

# Register your models here.

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BarrowedBook)
admin.site.register(User)
