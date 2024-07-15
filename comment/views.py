from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DeleteView, CreateView, UpdateView

from comment.forms import CommentForm, RateForm
from comment.models import Comment, Rate
from doctor.models import Doctor
from doctor.models import Appointment
# Create your views here.


class CreateCommentView(LoginRequiredMixin, CreateView):
    template_name = "comment/details_comment.html"
    form_class = CommentForm
    model = Comment
    success_url = reverse_lazy('doctor:home')

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        try:
            self.parent_id = kwargs['parent_id']
        except:
            pass
        self.doctor = Doctor.objects.get(pk=self.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        end_comment = form.save(commit=False)
        end_comment.doctor = self.doctor
        end_comment.user = self.request.user
        try:
            end_comment.parent = Comment.objects.get(pk=self.parent_id)
        except:
            pass
        is_appointment = Appointment.objects.filter(doctor=self.doctor, user=self.request.user)
        if not is_appointment:
            end_comment.content = f"{end_comment.content} \n You do not Appointment with this doctor"
        end_comment.save()
        return redirect(reverse('doctor:explore', kwargs={'pk': self.doctor.id}))


class RateClassView(LoginRequiredMixin, CreateView):
    template_name = "comment/rate.html"
    form_class = RateForm
    model = Rate

    def dispatch(self, request, *args, **kwargs):
        self.doctor_id = kwargs['doctor_id']
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        end_rate = form.save(commit=False)
        end_rate.user = self.request.user
        end_rate.doctor = self.doctor_id
        return redirect(reverse('doctor:explore', kwargs={'pk': self.doctor_id}))





class DeleteCommentView(LoginRequiredMixin, DeleteView):
    template_name = "comment_delete"


class UpdateCommentView(LoginRequiredMixin, UpdateView):

    form_class = CommentForm
    model = Comment
    context_object_name = "comment"
    success_url = reverse_lazy('doctor:home')

    def form_valid(self, form):
        self.object = form.save()
        return redirect('doctor:explore', pk=self.object.doctor.id)

    def get_template_names(self):
        if "/update-comment/" in self.request.path:
            template_name = "comment/details_comment.html"
            return template_name
        elif "/update-reply/" in self.request.path:
            template_name = "comment/reply_comment.html"
            return template_name

