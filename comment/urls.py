from django.urls import path
from comment.views import CreateCommentView, UpdateCommentView\
   , RateClassView

app_name = "comment"


urlpatterns = [
   path("create-comment/<int:pk>/", CreateCommentView.as_view(), name="create_comment"),
   path("create-comment/<int:pk>/<int:parent_id>/", CreateCommentView.as_view(), name="create_comment"),
   path("update-comment/<int:pk>/", UpdateCommentView.as_view(), name="update_comment"),
   path("update-reply/<int:pk>/", UpdateCommentView.as_view(), name="update_reply"),
   path("rate/<int:doctor_id>/", RateClassView.as_view(), name="update_reply"),


   ]
