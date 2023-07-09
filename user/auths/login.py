from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.cache import cache
from django.contrib import messages


from user.forms import LoginForm
from user.models import User



def login_user(request):
    form = LoginForm()
    if request.method == 'GET':
        cache.set('next', request.GET.get('next', None))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user = User.objects.get(email=email)
                print(user)
                req = authenticate(request,email=email,password=password)
                if req:
                    login(request,req)
                    messages.success(request,'Logged in successfully')

                    # next_url = cache.get('next')
                    # if next_url == None:
                    #     return redirect("index")
                    # return redirect(next_url)

                elif user is not None or user.password is None:
                    print('Incorrect password')
                    messages.error(request, "Incorrect password")
            except:
                messages.error(request, f"User with email: {email} does not exist")

    return render(request, 'login.html', {'form': form})
