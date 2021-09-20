from django.core.checks.messages import Error
from django.db import models
from django.http import response, JsonResponse
from django.http.request import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView, ListView,DetailView,UpdateView
from django.views.generic.base import View
from .models import Comentarios, Puntuacion, sitio
from apps.controlUsuarios.models import Usuario
from .forms import SitioForm, ComentarioForm
from django.urls.base import reverse_lazy
from django.urls import reverse
import json
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

class MostrarSitio(DetailView):
    model = sitio
    modelo2 = Puntuacion
    template_name = "web/detalle_sitio.html"    

    def get_context_data(self, **kwargs):
        context = super(MostrarSitio, self).get_context_data(**kwargs)                
        try:
            valores = self.modelo2.objects.filter(sitio__id=self.kwargs['pk'])
            sumatoria = 0
            for valor in valores:                      
                sumatoria += valor.Puntuacion
            context['puntuacion'] = str(sumatoria)
            context['cantidad'] = self.modelo2.objects.filter(sitio__id=self.kwargs['pk']).count() 
            
        except:
            context['puntuacion'] = 0        
            context['cantidad'] = 0           
        
        return context

class crearComentario(CreateView):
    model = Comentarios    
    form_class = ComentarioForm
    template_name = "web/crear_comentario.html"  
    success_url = reverse_lazy("detalle_sitio_publico")

    def post(self, request, *args, **kwargs) :      
        id_sitio = request.POST.get("sitio")
        user = Usuario.objects.get(id=request.POST.get("usuario"))
        sitio_re = sitio.objects.get(id=id_sitio)
        form = self.form_class(request.POST)
        if form.is_valid():
            comentario_nuevo = Comentarios(
                comentario = request.POST.get("comentario"),
                sitio = sitio_re,
                usuario = user
            )       
            comentario_nuevo.save()        
            mensaje = "comentario creado correctamente"
            error = "no hay error"
        else:
            mensaje = "No se pudo crear el comentario"
            error = form.errors
            
        response = JsonResponse({'mensaje':mensaje, 'error':error,'id_sitio':id_sitio})
        response.status_code = 201
            
        # return response
        return HttpResponseRedirect(reverse('detalle_sitio_publico', args=(id_sitio)))

class Puntuacion(View):
    model = Puntuacion        
    template_name = "web/crear_comentario.html"  
    success_url = reverse_lazy("detalle_sitio_publico")

    def get(self, request, *args, **kwargs) :      
        id_sitio = request.GET.get("sitio")
        id_usuario = request.GET.get("usuario")
        value = request.GET.get("valor")
        sitio_re = sitio.objects.get(id=id_sitio)
        usuario_re = Usuario.objects.get(id=id_usuario)
        puntuacion = self.model(Puntuacion=value,sitio = sitio_re, usuario = usuario_re)
        puntuacion.save()    
        mensaje = "puntuacion creado correctamente"
        error = "no hay error"
        response = JsonResponse({'mensaje':mensaje, 'error':error,'id_sitio':id_sitio})
        response.status_code = 201
        
        return HttpResponseRedirect(reverse('detalle_sitio_publico', args=(id_sitio)))

class ListarComentarios(TemplateView):
    model = Comentarios
    
    def get(self, request, *args, **kwargs):
        
        id_sitio = request.GET.get("sitio")          
        try:              
            comentarios_sitio = self.model.objects.filter(sitio__id=id_sitio)        
            lista_comentarios = []       
            for comentario in comentarios_sitio:
                data_comentario = {}
                data_comentario['comentario'] = comentario.comentario
                data_comentario['usuario'] = comentario.usuario.nombre
                lista_comentarios.append(data_comentario)
            data = json.dumps(lista_comentarios)
        except Exception as e:
            return render(request, self.template_name)
        
        return HttpResponse(data,'application/json')
    
    # def post(self, request, *args, **kwargs) :      
    #     id_sitio = request.POST.get("sitio")
    #     user = Usuario.objects.get(id=request.POST.get("usuario"))
    #     sitio_re = sitio.objects.get(id=id_sitio)
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         comentario_nuevo = Comentarios(
    #             comentario = request.POST.get("comentario"),
    #             sitio = sitio_re,
    #             usuario = user
    #         )       
    #         comentario_nuevo.save()        
    #         mensaje = "comentario creado correctamente"
    #         error = "no hay error"
    #     else:
    #         mensaje = "No se pudo crear el comentario"
    #         error = form.errors
            
    #     response = JsonResponse({'mensaje':mensaje, 'error':error,'id_sitio':id_sitio})
    #     response.status_code = 201
            
    #     return HttpResponse(response)