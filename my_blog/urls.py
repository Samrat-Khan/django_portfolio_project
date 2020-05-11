from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns = [
    path('', views.Blog, name='Blog'),
    path('<int:blog_id>', views.Details, name="Details"),
]
