from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile

from django.contrib.auth.decorators import login_required

def register(request):
    

    if request.method=='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account saved {username}')
    
            return redirect('blog-home')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    return render(request, 'users/profile.html', {'profile': profile})
    #profile = Profile.objects.get(user=request.user)
    #return render(request, 'users/profile.html', {'profile': profile})