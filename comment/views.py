from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, CreateView, UpdateView

from comment.forms import CommentForm
from comment.models import Comment
from doctor.models import Doctor
# Create your views here.


class CreateCommentView(LoginRequiredMixin, CreateView):
    template_name = "comment/details_comment.html"
    form_class = CommentForm
    model = Comment

    success_url = reverse_lazy('doctor:home')

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        self.doctor = Doctor.objects.get(pk=self.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        end_comment = form.save(commit=False)
        end_comment.doctor = self.doctor
        end_comment.user = self.request.user
        end_comment.save()
        return super(CreateCommentView, self).form_valid(form)


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    template_name = "comment_delete"


class UpdateCommentView(LoginRequiredMixin, UpdateView):
    template_name = "comment/details_comment.html"
    form_class = CommentForm
    model = Comment
    context_object_name = "comment"
    success_url = reverse_lazy('doctor:home')
