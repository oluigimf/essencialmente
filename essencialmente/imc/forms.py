from django import forms
from .models import AvaliarIMC

class AvaliarIMCForm(forms.ModelForm):
    class Meta:
        model = AvaliarIMC
        fields = ["cpf", "nome", "sexo", "data_nascimento", "escola", "peso", "altura", "foto"]
