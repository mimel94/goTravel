from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.contrib.auth import login,logout

from .models import Usuario
from .forms import FormularioLogin, controlUsuarioForm

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.views.generic.edit import  FormView
from django.views.generic import ListView, CreateView,TemplateView

# Create your views here.
class Login(FormView):
    template_name = 'web/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('dashboard')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
    
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class Dashboard(TemplateView):        
    template_name="dashboard/index.html"
    

class CrearUsuario(CreateView):
    model = Usuario
    template_name = 'web/registro.html'
    form_class = controlUsuarioForm
    success_url = reverse_lazy('login')
