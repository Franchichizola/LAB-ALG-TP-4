from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import ComentarioForm
from .forms import CustomUserCreationForm 
from django.contrib import messages
from .forms import PostForm
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-fecha_creacion")
    return render(request, "blog/index.html", {"posts": posts})


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

def registro_usuario(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"¡Cuenta creada para {username}! Ahora puedes iniciar sesión.")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/registro.html", {"form": form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_index')
    else:
        form = PostForm()
    
    return render(request, 'blog/crear_post.html', {'form': form})