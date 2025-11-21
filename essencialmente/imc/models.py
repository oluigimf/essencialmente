from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class AvaliarIMC(models.Model):
    SEXO_CHOICES = [("M", "Masculino"), ("F", "Feminino")]

    cpf = models.CharField(primary_key=True, max_length=11, unique=True, null=False, blank=False)
    nome = models.CharField(max_length=120, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    escola = models.CharField(max_length=150, null=False, blank=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(Decimal("0.1"))])
    altura = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(Decimal("0.1"))])
    foto = models.ImageField(upload_to="imc_fotos/", null=False, blank=False)
    valor_imc = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        if self.peso and self.altura:
            altura_float = float(self.altura)
            imc_calc = float(self.peso) / (altura_float ** 2)
            self.valor_imc = Decimal(imc_calc).quantize(Decimal("0.01"))
        super().save(*args, **kwargs)

    @property
    def classificacao(self):
        imc = float(self.valor_imc)
        if imc < 18.5: return "Abaixo do Normal"
        elif imc < 25: return "Normal"
        elif imc < 30: return "Sobrepeso"
        elif imc < 35: return "Obesidade Grau 1"
        elif imc < 40: return "Obesidade Grau 2"
        else: return "Obesidade Grau 3"

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf} - IMC: {self.valor_imc}"

    class Meta:
        verbose_name = "Avaliação de IMC"
        verbose_name_plural = "Avaliações de IMC"
        ordering = ["nome"]
