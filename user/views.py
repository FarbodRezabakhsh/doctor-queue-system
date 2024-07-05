from django.shortcuts import render
from django.views import View


# Create your views here.


class CustomLoginView(View):
    def get(self, request):
        return render(request, template_name='user/login.html')