from django.contrib import admin
from comment.models import Comment
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed on the change form
    def get_fields(self, request, obj=None):
        return ["user", "doctor", "content", "approach", "parent"]

    # Specify the fields to be displayed on the change list
    def get_list_display(self, request):
        return ["user", "doctor", "content", "approach", "parent"]
