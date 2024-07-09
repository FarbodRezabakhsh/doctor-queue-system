from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from comment.forms import CommentForm
from doctor.models import Doctor
# Create your views here.


class CreateCommentView(LoginRequiredMixin, View):
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs['pk']
        print(self.pk)
        self.doctor = Doctor.objects.get(pk=self.pk)
        print(self.doctor)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            endcomment = form.save(commit=False)
            endcomment.doctor = self.doctor
            endcomment.user = request.user
            endcomment.save()
        return redirect('doctor:home')


