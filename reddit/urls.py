from django.urls import path
from . import views

app_name = "reddit"
urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('delete/<int:post_id>', views.DeleteView.as_view(), name='delete'),
    path('<str:user>/<int:pk>', views.DetailView.as_view(), name="detail"),
    path('<str:user>/', views.PublicProfileView.as_view(), name="profile"),
]
