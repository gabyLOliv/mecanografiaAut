from django.conf import settings
from django.contrib.auth import login, authenticate

from django.urls import reverse_lazy
from django.shortcuts import render, resolve_url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from . import models
from core import models as core_models
from core import forms
from .forms import NotificacaoForm

from django.shortcuts import redirect


def login(request):
	
	matricula = request.POST['matricula']
	password = request.POST['password']
	form = forms.UUIDUserForm(request.POST)
	if form.is_valid():
		user = authenticate(matricula=matricula, password=password)
		if not user is None:
			login(user)

def index(request):

	if request.user.is_authenticated:
		if request.user.tipo_user == 0:
			return redirect(reverse_lazy('user-form'))
		else:
			return redirect(reverse_lazy('solicitacoes'))

	return render(request, 'index.html')


def cadastro(request):
	return render(request, 'cadastro.html')


class Forms(LoginRequiredMixin, CreateView):

    model = models.Formulario
    fields = ( 'nome', 'disciplina', 'numero_de_paginas','numero_de_copias', 'tipo')
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
	    user = self.request.user
	    form.instance.user = user
	    return super(Forms, self).form_valid(form)


def solicitacoes(request):

	context = {
		'forms': models.Formulario.objects.all()
	}

	return render(request, 'solicitacoes.html', context)


# @login_required(login_url='/login/')
# def forms_delete(request, pk):

#     form = get_object_or_404(models.Formulario, id=pk)

#     if request.method == 'POST':
        
# 	    form.delete()
		
# 	    # form = NotificacaoForm(request.POST)
# 	    # if form.is_valid():

# 	    # 	noti = form.save()
# 	    # 	noti.tipo = form.tipo
# 	    # 	noti.user = form.user
# 	    # 	noti.save()

# 	    # 	form = NotificacaoForm()
# 	    return redirect(reverse_lazy('solicitacoes'))


#     context = {
#         'form': form
#     }
#     return render(request, 'solicitacoes.html', context)


@login_required(login_url='/login/')
def forms_delete(request, pk):

    formulario = get_object_or_404(models.Formulario, id=pk)

    if request.method == 'POST':
        formulario.delete()
        notificacao = models.Notificacao(tipo=formulario.tipo, user=formulario.user)
        notificacao.save()
        # form = NotificacaoForm(request.POST)
        # if form.is_valid():

        #     var = formulario.copy()
        #     noti = form.save()
        #     noti.tipo = var.tipo
        #     noti.user = var.user
        #     noti.save()

        return redirect(reverse_lazy('solicitacoes'))

    context = {
        'formulario': formulario
    }
    return render(request, 'forms-delete.html', context)
