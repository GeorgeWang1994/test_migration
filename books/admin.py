from django.contrib import admin

from books.models import Books, Publish

# Register your models here.
admin.site.register(Books)
admin.site.register(Publish)
