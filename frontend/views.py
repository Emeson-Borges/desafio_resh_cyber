from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.contrib import messages

API_BASE_URL = 'http://127.0.0.1:8000/api/users/'
 
  
@csrf_exempt
def login_view(request):
  if request.method == 'POST':
      data = {
          'username': request.POST['username'],
          'password': request.POST['password'],
      }
      
      user = authenticate(request, username=data['username'], password=data['password'])
      
      if user is not None:
          login(request, user)
          return redirect('dashboard_view')
      else:
          error_message = "Erro ao fazer login. Verifique suas credenciais e tente novamente."
          return render(request, 'login/login.html', {'error_message': error_message})

  return render(request, 'login/login.html')

@csrf_exempt
def register_view(request):
  if request.method == 'POST':
        username  = request.POST['username']
        email     = request.POST['email']
        password  = request.POST['password']
      
        try:
            user = User.objects.create_user(username=username, email=email,  password=password)
            user.save()

            return redirect('login_view')
        except:
            error_message = "Erro ao registrar usuário. Verifique os dados e tente novamente."
            return render(request, 'register/register.html', {'error_message': error_message})

  return render(request, 'register/register.html')

@login_required
def dashboard_view(request):
  user_data = {'username': request.user.username, 'email': request.user.email, 'password': request.user.password}
  return render(request, 'dashboard/dashboard.html',  {'user_data': user_data})


@login_required
def change_email_view(request):
  if request.method == 'POST':
    new_email = request.POST.get('new_email')
    if new_email:
      request.user.email = new_email
      request.user.save()
      messages.success(request, 'E-mail alterado com êxito.')
      
    else:
      messages.error(request, 'Por favor, forneça um novo e-mail válido.')
    return redirect('change_email')
  return render(request, 'change_email/change_email.html')

@login_required
def change_password_view(request):
  if request.method == 'POST':
    new_password = request.POST.get('new_password')
    if new_password:
      request.user.set_password(new_password)
      request.user.save()
      messages.success(request, 'Password alterado com êxito.')
      return render(request, 'login/login.html')
    else:
      messages.error(request, 'Por favor, forneça um novo Password válido.')
      
    return redirect('change_password')
  return render(request, 'change_password/change_password.html')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    logout(request)
    return redirect('login_view')
  
@csrf_exempt
def delete_account_view(request):
  if request.method == 'POST':
    if request.user.is_authenticated and request.user == request.user:
      request.user.delete()     
      return redirect('login_view')
  return render(request, 'login/login.html')