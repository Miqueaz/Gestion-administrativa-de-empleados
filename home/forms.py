from django import forms


class InicioSesion(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe tu username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "placeholder":"escribe tu password"}))