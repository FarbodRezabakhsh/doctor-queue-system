from django.urls import path
from comment.views import CreateCommentView

app_name = "comment"


urlpatterns = [
   path("create-comment/<int:pk>/", CreateCommentView.as_view(), name="create_comment")
   ]
