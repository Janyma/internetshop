from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy



'''def login(request):
    if request.user.is_authenticated:
        return render(request, 'shopview.html')
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            return render(request, 'shopview.html')

    form=AuthenticationForm()
    return render(request, 'loginsite.html', {'form':form})'''

class Register(CreateView):
     form_class=UserCreationForm
     success_url=reverse_lazy("loginsite")
     template_name="registration.html"


def shopview(request):
  #  if request.user.is_authenticated:
       return render(request, 'shopview.html')
   # else:
     #   return redirect('shopview')
