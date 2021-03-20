# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/register_view")
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

@login_required
def register_view(request):
    users = User.objects.all()
    return render(request,'viewUsers.html',{'users':users})
