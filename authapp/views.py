from django.shortcuts import render,redirect

# Create your views here.
def auth(request):
    return render(request,"auth/login.html")
def dashboard(request):
    if request.user.is_authenticated:
        # If the user has the appropriate permissions, render the dashboard.
        return render(request,"auth/dashboard.html")
    else:
        # If the user does not have access, redirect them to an error page or a different page.
        return redirect("login")