from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog_index"),
    path("post/<slug:slug>/", views.detalle_post, name="detalle_post"),
]