from django.contrib import admin

from .models import Post, Blog

from markdownx.widgets import AdminMarkdownxWidget

class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description']
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fields to search in change list
    search_fields = ['title', 'description', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}

    formfield_overrides = {
        Post.content: {'widget': AdminMarkdownxWidget},
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Blog)