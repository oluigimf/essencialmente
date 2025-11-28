from django.shortcuts import render, redirect
from .forms import AvaliarIMCForm
from .models import AvaliarIMC

#tela inicial
def index(request):
    return render(request, "index.html")

#funcao que chama a tela de cadastro e que calcula o imc e mostra
def avaliar_imc(request):
    imc = None
    classificacao = None
    avaliacao = None

    if request.method == "POST":
        form = AvaliarIMCForm(request.POST, request.FILES)
        if form.is_valid():
            avaliacao = form.save()     # calcula o IMC no save()
            imc = avaliacao.valor_imc
            classificacao = avaliacao.classificacao
    else:
        form = AvaliarIMCForm()

    return render(request, "avaliarIMC.html", {
        "form": form,
        "imc": imc,
        "classificacao": classificacao,
        "avaliacao": avaliacao,
    })

#tela de listar os cadastrados
def listar_cadastrados(request):
    sexo = request.GET.get("sexo")
    if sexo in ["M", "F"]:
        cadastrados = AvaliarIMC.objects.filter(sexo=sexo)
    else:
        cadastrados = AvaliarIMC.objects.all()
    return render(request, "cadastradosLista.html", {"cadastrados": cadastrados, "sexo_selecionado": sexo})

#tela teste da juylia
def julia_zaffari(request):
    return render(request, 'telaTesteJZ.html')