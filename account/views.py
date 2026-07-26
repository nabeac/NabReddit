from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .form import UserRegisterForm

class UserRegisterView(View):
    form_class = UserRegisterForm
    template = 'account/register.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form':form})
    
    def post(self, request):  
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request,'ثبت شد' ,'success')
            return redirect('reddit:home')
        
        return render(request, self.template, {'form':form})
        
        