from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        helps_text = {llave: "" for llave in fields}
        
class FormularioEdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar"]
    
    