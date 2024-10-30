from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from user.forms import ProfileUpdate, UpdateUserForm, UserRegister


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)  # pass the POST data to the form
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'User with username: {form.cleaned_data['username']} created successfully!',
            )
            return redirect('login')
        else:
            messages.error(request, f'Na Bacha Aisay nahi chalay ga!')

    else:
        form = UserRegister()

    context = {'title': 'Register', 'form': form}
    return render(request, 'user/register.html', context)


@login_required(login_url='login')
def profile(request):
    if request.method == "POST":

        #! Populate the forms by passing the instance
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = ProfileUpdate(
            request.POST, request.FILES, instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Form updated Successfully!')

        else:
            messages.error(request, f'An Error Occured')

    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

    context = {
        'title': 'Profile',
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'user/profile.html', context)
