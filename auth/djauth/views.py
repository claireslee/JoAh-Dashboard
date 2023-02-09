
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin


class ProtectedView(LoginRequiredMixin, View):
    login_url = "login"
    redirect_field_name = "redirect_to"
    
    def get(self, req, *args, **kwargs):
        user = req.user
        
        if isinstance(user, AnonymousUser):
            return HttpResponse("You do not have access!")
        else:
            return HttpResponseRedirect("redirect_to")
        

class LoginView(View):
    form_class = LoginForm
    
    def post(self, req, *args, **kwargs):
        form = self.form_class(data=req.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(req, username=username, password=password)
            
            if user is not None:
                login(req, user)
                redirect_to = "http://127.0.0.1:5501/teacherDashboard.html"
                
                if redirect_to is None:
                    return HttpResponseRedirect("You've logged in.")
                else: 
                    return HttpResponseRedirect(redirect_to)
            else: 
                return HttpResponse("Invalid username or password. Please try again.")
        else:
            return HttpResponse("Please provide both your username and password.")
    
    def get(self, req, *args, **kwargs):
        form = self.form_class()
        return render(
            req,
            "djauth/login.html",
            {
                "form": form
            },
        )
    
class LogoutView(View):
    def get(self, req, *args, **kwargs):
        user = req.user
        if isinstance(user, AnonymousUser):
            return HttpResponse("You haven't logged in so you can't log out?!!")
        else:
            logout(req)
            return HttpResponse("Successfully logged out")
        
    

    
    
# Create your views here.
