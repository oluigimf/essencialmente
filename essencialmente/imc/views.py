from django.shortcuts import render, redirect
from .forms import AvaliarIMCForm
from .models import AvaliarIMC

def index(request):
    return render(request, "index.html")

def avaliar_imc(request):
    if request.method == "POST":
        form = AvaliarIMCForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save() 
            return redirect("imc:resultado_imc", cpf=obj.cpf)
    else:
        form = AvaliarIMCForm()
    return render(request, "avaliarIMC.html", {"form": form})

def resultado_imc(request, cpf):
    avaliacao = AvaliarIMC.objects.get(cpf=cpf)
    return render(request, "avaliarIMC.html", {"avaliacao": avaliacao})

def listar_cadastrados(request):
    sexo = request.GET.get("sexo")
    if sexo in ["M", "F"]:
        cadastrados = AvaliarIMC.objects.filter(sexo=sexo)
    else:
        cadastrados = AvaliarIMC.objects.all()
    return render(request, "ListarCadastradosIMC.html", {"cadastrados": cadastrados, "sexo_selecionado": sexo})
