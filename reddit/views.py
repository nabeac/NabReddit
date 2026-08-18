from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . models import Post


class HomeView(View):
    
    def get(self, request):
        post = Post.objects.all()
        return render(request, "reddit/home.html", {'post': post})


class DetailView(View):

    def get(self, request, user, pk):
        # user = User.objects.get(username=user)
        post = Post.objects.get(pk=pk, author__username=user)
        return render(request, "reddit/detail.html", {'post': post})
    

class PublicProfileView(View):

    def get(self, request, user):
        user = get_object_or_404(User, username=user)
        # user = User.objects.get(username=user)
        post = Post.objects.filter(author=user)
        return render(request, "reddit/profile.html", {'post': post, 'author': user})

class DeleteView(LoginRequiredMixin, View):
     
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if post.author == request.user:
            post.delete()
            messages.success(request,'با موفقیت حذف شد' ,'success')
            return redirect('reddit:home')
        messages.success(request,'مگه مال توعه آخه' ,'worning')
        return redirect('reddit:home')