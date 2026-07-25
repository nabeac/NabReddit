from django.shortcuts import render
from django.views import View
from .form import UserRegisterForm

class UserRegisterView(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'account/register.html', {'form':form})
    def post(self, request):  
         pass