from django.contrib import admin
from .models import Review


class ListReviews(admin.ModelAdmin):
    list_display = ('url_id', 'title','category', 'author', 'public')
    list_display_links = ('url_id', 'title')
    search_fields = ('title', 'category', 'author')
    list_filter = ('category', 'author')
    list_per_page = 10

admin.site.register(Review, ListReviews)
