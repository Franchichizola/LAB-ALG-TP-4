from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.forms import inlineformset_factory
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "archivo_multimedia"]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class ComentarioForm(forms.Form):
    texto = forms.CharField(label="", widget=forms.Textarea(attrs={'rows': 4}))
