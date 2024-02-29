from django import forms
 # Planillas
class cursoform(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class estudianteform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class profesform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    profesion = forms.CharField(max_length=30)

class busca(forms.Form):
    nombre = forms.CharField(max_length=20)