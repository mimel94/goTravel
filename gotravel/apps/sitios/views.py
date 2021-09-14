from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView, ListView,DetailView,UpdateView
from .models import sitio
from .forms import SitioForm
from django.urls.base import reverse_lazy
# Create your views here.

class Index(ListView):
    template_name = "web/index.html"
    model = sitio
    paginate_by = 10
    

class CrearSitio(CreateView):
    model = sitio
    template_name = "dashboard/crear_sitio.html"
    form_class = SitioForm
    success_url = reverse_lazy('listar_sitios_propios')   

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return  redirect("listar_sitios_propios")

class ListarSitiosPropios(ListView):
    model = sitio
    template_name = "dashboard/listar_sitios_propios.html"
    paginate_by = 10

    def get_queryset(self):
        consulta = self.model.objects.filter(usuario=self.request.user)
        return consulta

class ActualizarSitio(UpdateView):
    model = sitio
    template_name = "dashboard/actualizar_sitio.html"
    form_class = SitioForm
    success_url = reverse_lazy('listar_sitios_propios')
