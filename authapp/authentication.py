from django.contrib.auth import authenticate, login,logout as logoutUser
from django.shortcuts import render,redirect
def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or do something else
            return redirect("dashboard")
        else:
            error_message = 'Invalid credentials. Please try again.'
            return render(request, 'auth/login.html', {'error_message': error_message})

    else:
        return render(request,"auth/login.html")
def logout(request):
    logoutUser(request)
    return redirect("login")  