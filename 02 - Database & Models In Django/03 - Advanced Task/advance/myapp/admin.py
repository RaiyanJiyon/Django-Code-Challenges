from django.contrib import admin
from .models import Publisher, Book

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'publisher')
    list_filter = ('publication_date', 'publisher')
    search_fields = ('title', 'author')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)