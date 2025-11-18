from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        print("POST")
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_expenses')
        else:
            error = "Invalid username or password."
            return render(request, 'accounts/login.html', {'error': error})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')