from django import forms
from .models import AvaliarIMC

class AvaliarIMCForm(forms.ModelForm):
    class Meta:
        model = AvaliarIMC
        fields = ["cpf", "nome", "sexo", "data_nascimento", "escola", "peso", "altura", "foto"]
        widgets = {
            "cpf": forms.TextInput(attrs={"class": "input-field"}),
            "nome": forms.TextInput(attrs={"class": "input-field"}),
            "sexo": forms.Select(attrs={"class": "input-field"}),
            "data_nascimento": forms.DateInput(attrs={"class": "input-field", "type": "date"}),
            "escola": forms.TextInput(attrs={"class": "input-field"}),
            "peso": forms.NumberInput(attrs={"class": "input-field"}),
            "altura": forms.NumberInput(attrs={"class": "input-field"}),
            "foto": forms.FileInput(attrs={"class": "input-field"}),
        }
