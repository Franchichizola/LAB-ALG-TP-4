from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog_index"),
    path("post/crear_post/", views.crear_post, name="crear_post"),
    path("post/<slug:slug>/", views.detalle_post, name="detalle_post"),
]