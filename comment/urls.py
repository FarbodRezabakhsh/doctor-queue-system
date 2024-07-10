from django.urls import path
from comment.views import CreateCommentView, UpdateCommentView

app_name = "comment"


urlpatterns = [
   path("create-comment/<int:pk>/", CreateCommentView.as_view(), name="create_comment"),
   path("update-comment/<int:pk>/", UpdateCommentView.as_view(), name="update_comment")
   ]
