
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.views.generic import TemplateView

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from contextlib import redirect_stderr, redirect_stdout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Student
from .forms import StudentForm
from .models import Announcement
from .forms import AnnouncementForm
from .forms import HomeForm
from django.contrib import messages
from django.http import HttpResponse



def mainpage(request):
    
    all_students = Student.objects.all
    return render(request, 'djauth/mainpage.html',{'all':all_students})

def aboutUs(request):
    return render(request, 'djauth/aboutUsTab.html')
    
def resources(request):
    return render(request, 'djauth/resources.html')

def calendar(request):
    return render(request, 'djauth/calendar.html')

def programs(request):
    return render(request, 'djauth/programs.html')

def contactus(request):
    return render(request, 'djauth/contactus.html')

@login_required(login_url="/login")
def teacherDash(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        all_students = Student.objects.all # assign all data in db to the variable
        return render(request, 'djauth/teacherDash.html', {'all':all_students})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
   

@login_required(login_url="/login")
def studentDashboard(request):
    all_students = Student.objects.all
    return render(request, 'studentDashboard/studentDashboard.html', {'all':all_students})

def loggedin_view(request):
    
    all_students = Student.objects.all
    usergroup = None
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
        
@login_required(login_url="/login")
def teacherCalendar(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return render(request, 'djauth/teacherCalendar.html')
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
   
    
@login_required(login_url="/login")
def teacherAnnouncement(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return render("djauth/teacherAnnouncement.html")
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
   

@login_required(login_url="/login")
def studentDisplay(request):
    all_students = Student.objects.all
    return render(request, 'djauth/studentDisplay.html',{'all':all_students} )

@login_required(login_url="/login")
def createTest(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return render("djauth/addQuestion.html")
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")


@login_required(login_url="/login")
def studentCalendar(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return render(request, "studentDashboard/studentCalendar.html")
   

@login_required(login_url="/login")
def studentAnnouncement(request):
    if request.user.is_authenticated:
            usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return render("studentDashboard/studentAnnouncement.html")


@login_required(login_url="/login")
def startExam(request):
    if request.user.is_authenticated:
            usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return render("studentDashboard/startExam.html")

@login_required(login_url="/login")
def addStudent(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        if request.method == "POST":
            form = StudentForm(request.POST or None) 
            if form.is_valid():
                form.save()
                User.objects.create_user(username=request.POST['username'],
                                    password=request.POST['passwd'] )
            else:
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']  
                username = request.POST['username']
                passwd = request.POST['passwd']  
                classname = request.POST['classname']    
                gradelvl = request.POST['gradelvl']  
                # email = request.POST['email']  
                
                messages.success(request, ('There was an error in your form! Please try again...'))
                return render(request, 'addStudent.html', {'firstname': firstname,
                                                    'lastname': lastname,
                                                    'username': username,
                                                    'passwd': passwd,
                                                    'classname': classname,
                                                    'gradelvl': gradelvl,
                                                    # 'email': email,
                                                    })
                
            
            messages.success(request, ('Student has been added to the database!'))
            
            
            
            return HttpResponseRedirect("/teacherDash")
    
    # otherwise, just return the page bc no info submission
        else:
            return render(request, 'djauth/addStudent.html', {})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    # if someone posts + fill out form ... 
    
# Create your views here.

def home(request):
    if request.user.is_authenticated:
            usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        if request.method == 'POST':
            print(request.POST)
            questions=QuesModel.objects.all()
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                total+=1
                print(request.POST.get(q.question))
                print(q.ans)
                print()
                if q.ans ==  request.POST.get(q.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            percent = score/(total*10) *100
            context = {
                'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
            }
            return render(request,'studentDashboard/result.html',context)
        else:
            questions=QuesModel.objects.all()
            context = {
                'questions':questions
            }
            return render(request,'studentDashboard/home.html',context)


def addQuestion(request): 
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return HttpResponseRedirect('/confirmation')
        context={'form':form}
        return render(request,'djauth/addQuestion.html',context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
      
        
    
def confirmation(request):
    if request.user.is_authenticated:
            usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return HttpResponseRedirect("/confirmation")

def result(request):
    if request.user.is_authenticated:
            usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return HttpResponseRedirect("/studentDashboard/result")
    



    
def dash(request):
    usergroup = None
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

def acttestprep(request):
    return render(request, 'djauth/acttestprep.html')

def algebra1(request):
    return render(request, 'djauth/algebra1.html')

def apcalc(request):
    return render(request, 'djauth/apcalc.html')

def aphistory(request):
    return render(request, 'djauth/aphistory.html')

def aplang(request):
    return render(request, 'djauth/aplang.html')

def geometry(request):
    return render(request, 'djauth/geometry.html')

def jr1(request):
    return render(request, 'djauth/jr1.html')

def jr2(request):
    return render(request, 'djauth/jr2.html')

def jr3(request):
    return render(request, 'djauth/jr3.html')

def satadvanced(request):
    return render(request, 'djauth/satadvanced.html')

def satbasic(request):
    return render(request, 'djauth/satbasic.html')

def sattestprep(request):
    return render(request, 'djauth/sattestprep.html')

def tutor(request):
    return render(request, 'djauth/tutor.html')


    
def studentAnnouncement(request):
    all_announcements = Announcement.objects.all
    return render(request, 'studentDashboard/studentAnnouncement.html', {'all_announcements': all_announcements})

def teacherAnnouncement(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Your Announcement Has Been Uploaded!'))
        
        return HttpResponseRedirect("/teacherDash")
        #return render(request, 'teacherAnnouncement.html', {})
    
    else:
        return render(request, 'djauth/teacherAnnouncement.html', {})
    
                
    