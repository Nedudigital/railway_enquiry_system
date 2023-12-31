from django.shortcuts import render, redirect
from django.contrib import messages


from user.forms import UserRegisterForm
from user.models import User



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            # return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
