from django import forms

class ComentarioForm(forms.Form):
    texto = forms.CharField(label="", widget=forms.Textarea(attrs={'rows': 4}))