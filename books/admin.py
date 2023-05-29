from django.contrib import admin
from books import models

# Register your models here.


@admin.register(models.Book)
class Book(admin.ModelAdmin):
    list_display = ('title_book', 'author', 'time_create', 'time_update')
