from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile 

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is now created! You can now Log In')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':

        u_editForm = UserEditForm(request.POST,instance=request.user )
        p_editForm = ProfileEditForm(request.POST,request.FILES,instance=request.user.profile )

        if u_editForm.is_valid() and p_editForm.is_valid():
            u_editForm.save()
            p_editForm.save()
            messages.success(request, f'Your Profile is Updated!')
            return redirect('profile')


    else:
        
        u_editForm = UserEditForm(instance=request.user)
        p_editForm = ProfileEditForm(instance=request.user.profile)
    context = {
        'u_form': u_editForm,
        'p_form': p_editForm
    }
    return render(request,'users/profile.html',context)



