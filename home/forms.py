from django import forms

class CreacionAuto(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    # fecha_creacion = forms.DateField()
    fecha_creacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))