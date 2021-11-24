from django.contrib import admin

from .models import Post, Question

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','body','created_on','active')
    list_filter = ('active', 'created_on')
    search_fields = ('body')
    actions = ['approve-comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post)
admin.site.register(Question)
