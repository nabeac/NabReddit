from django.shortcuts import render
from django.views import View


class HomeView(View):
    
    def get(self, request):
        return render(request, "reddit/home.html")

    def post(self):
        pass
# def home(request):
#     return render(request, 'reddit/home.html')