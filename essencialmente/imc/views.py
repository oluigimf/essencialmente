from django.shortcuts import render
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
            avaliacao = form.save()  # cálculo feito no save
            imc = avaliacao.valor_imc
            classificacao = avaliacao.classificacao
    else:
        form = AvaliarIMCForm()

    context = {
        "form": form,
        "imc": imc,
        "classificacao": classificacao,
        "avaliacao": avaliacao
    }

    return render(request, "avaliarIMC.html", context)

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