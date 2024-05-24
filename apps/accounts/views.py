from apps import ticketSales
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect(reverse(ticketSales.views.timesInfo))
        else:
            context = {
                "user": username,
                "error": "کاربر با این نام یافت نشد..."
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', {})

def logoutView(request):
    logout(request)
    if request.GET.get("next"):
        return render(request.GET.get("next"))
    return redirect(reverse(ticketSales.views.concertListView))

@login_required
def profileView(request):
    profile=request.user.profile
    context={
        "profile":profile
    }
    return render(request,"accounts/profile.html",context)