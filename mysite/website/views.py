from contextlib import redirect_stderr, redirect_stdout
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.
def home(request): 
    all_students = Student.objects.all # assign all data in db to the variable
    return render(request, 'home.html', {'all':all_students}) # pass var into home page -- context dictionary

def join(request):
    # if someone posts + fill out form ... 
    if request.method == "POST":
        form = StudentForm(request.POST or None) 
        if form.is_valid():
            form.save()
        
        else:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']  
            username = request.POST['username']
            passwd = request.POST['passwd']  
            classname = request.POST['classname']    
            email = request.POST['email']  
            
            messages.success(request, ('There was an error in your form! Please try again...'))
            return render(request, 'join.html', {'firstname': firstname,
                                                 'lastname': lastname,
                                                 'username': username,
                                                 'passwd': passwd,
                                                 'classname': classname,
                                                 'email': email,
                                                 })
        
        messages.success(request, ('Student has been added to the database!'))
        return redirect('home')
    
    # otherwise, just return the page bc no info submission
    else:
        return render(request, 'join.html', {})

def dashteacher(request): 
    return render(request, 'dashteacher.html', {})