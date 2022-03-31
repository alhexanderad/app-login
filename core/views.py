from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


'''Se necesita este codigo para el ingreso de login:'''
@login_required
def home(request):
  date_today = datetime.now().date()
  context ={
    'date_today': date_today
  }
  return render(request,'main/home.html', context)

def login_view(request):
  error_message = None
  form = AuthenticationForm()
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_director == False:
      login(request, user) 
      if request.GET.get('next'):
        return redirect(request.GET.get('next'))
      else:
        return redirect('home')
    else:
      error_message = 'Up something went wrong. Are you sure a producer?'
  return render(request, 'main/login.html',{'form':form, 'error_message':error_message})

def logout_view(request):
  logout(request)
  return redirect('home')