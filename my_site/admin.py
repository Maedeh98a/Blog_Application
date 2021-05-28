from django.contrib import admin
from my_site.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    list_filter = ['title', 'author']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
