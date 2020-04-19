from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CustomUserLoginForm, UserRegistrationForm
from .models import CustomUser

# Create your views here.


# def users_login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     email = request.POST['email']
#     user = authenticate(request, username=username,
#                         password=password, email=email)
#     if user is not None:
#         login(request, user)
#         redire
#         # Redirect to a success page.
#         ...
#     else:
# Return an 'invalid login' error message.
...


# def login(request):
#     return render(request, 'users/login.html')
def logout_view(request):
    logout(request)
    messages.info(request, f'Successfully logged out!')
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        CustomUser.objects.create_user(username, email, password)
        messages.info(request, f'Successfully registered.Log in now!')
        return redirect("/")

        # Redirect to a success page.

    elif request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, "registration/register.HTML", {'form': form})
