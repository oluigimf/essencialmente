from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from imc.views import index, avaliar_imc, julia_zaffari, listar_cadastrados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('avaliar_imc/', avaliar_imc, name="avaliar_imc"),
    path('teste/', julia_zaffari, name='telaTesteJZ'),
    path("listar/", listar_cadastrados, name="listar_cadastrados")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)