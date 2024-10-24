from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from user.forms import UserRegister


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)  # pass the POST data to the form
        if form.is_valid():
            form.save()
            messages.success(request, f'User with username: {form.cleaned_data['username']} created successfully!')
            return redirect('login')
        else:
            messages.error(request, f'Bhaag Jaa!')

    else:
        form = UserRegister()
    
    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'user/register.html', context)



def profile(request):
    context = {
        'title': 'Profile',
        # 'form': form
    }
    return render(request, 'user/profile.html', context)



