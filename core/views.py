from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from .models import UUIDUser
from .forms import UUIDUserForm, UUIDUserLoginForm

# User create
# - - - - - - - - - - - - - - - - - - - -
class UserCreateView(CreateView):
    model = UUIDUser
    template_name = 'cadastro.html'
    success_url = reverse_lazy('users-signin')
    form_class = UUIDUserForm


class UserLoginView(FormView):
  template_name = 'login.html'
  form_class = UUIDUserLoginForm
  success_url = '/'

  def post(self, request, *args, **kwargs):
    matricula = request.POST['matricula']
    password = request.POST['password']
    
    user = UUIDUser.objects.filter(matricula=matricula).first()

    username=user.username
    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
      login(request, authenticated_user)
      return redirect('/')

    return super().post(request, *args, **kwargs)
