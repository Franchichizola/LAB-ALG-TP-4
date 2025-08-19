from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-fecha_creacion")
    return render(request, "blog/index.html", {"posts": posts})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import ComentarioForm

def detalle_post(request, slug):
    post = get_object_or_404(Post, titulo_slug=slug)
    comentarios = post.comentario_set.all()  

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            Comentario.objects.create(
                post=post,
                usuario=request.user,  
                texto=form.cleaned_data["texto"]
            )
            return redirect("detalle_post", slug=post.titulo_slug)
    else:
        form = ComentarioForm()
    
    context = {
        "post": post,
        "comentarios": comentarios,
        "form": form,
    }
    return render(request, "blog/detalle_post.html", context)