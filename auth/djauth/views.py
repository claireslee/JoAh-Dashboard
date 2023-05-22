from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Student
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView
from django.contrib import messages
from .forms import PdfTestForm
from .models import PdfTest
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import PdfTest
from .forms import PdfTestForm
from django.forms import formset_factory
from django.forms import BaseFormSet

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from .models import Announcement
from .forms import AnnouncementForm
from .forms import HomeForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import DeleteExamForm


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
    username = request.user.username
    student = Student.objects.get(username=username)
    
    return render(request, 'studentDashboard/studentDashboard.html')


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
def studentDisplay(request):
    all_students = Student.objects.all
    return render(request, 'djauth/studentDisplay.html',{'all':all_students} )

@login_required(login_url="/login")
def examList(request):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'djauth/examList.html', context)

@login_required(login_url="/login")
def studentExamList(request):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'studentDashboard/studentExamList.html', context)

@login_required(login_url="/login")
# def examDetail(request, test_id):
#     test = Test.objects.get(id=test_id)
#     questions = test.questions.all()
#     context = {'test': test, 'questions':questions}
#     return render(request, 'djauth/examDetail.html', context)
def examDetail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    context = {'test': test, 'questions': questions}
    return render(request, 'djauth/examDetail.html', context)

@login_required(login_url="/login")
def studentExamDetail(request, test_id):
    if request.method == 'POST':
        print(request.POST)
        test = Test.objects.get(id=test_id)
        questions = test.questions.all()
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
        test = Test.objects.get(id=test_id)
        questions = test.questions.all()
        context = {
            'test': test, 'questions':questions
        }
        return render(request,'studentDashboard/studentExamDetail.html',context)

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
                    first_name = request.POST['first_name']
                    last_name = request.POST['last_name']
                    username = request.POST['username']
                    password = request.POST['password']
                    grade = request.POST['grade']
                    
                    
                    User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'] )
                    
                    
            
            # create and save student object
                    student = Student(first_name=first_name, last_name=last_name, username=username,
                            password=password, grade=grade)
                    student.save()


                    
                else:
                    first_name = request.POST['first_name']
                    last_name = request.POST['last_name']  
                    username = request.POST['username']
                    password = request.POST['password']    
                    grade = request.POST['grade'] 
                    # email = request.POST['email']  
                    
                    print(form.errors)
                    messages.success(request, ('There was an error in your form! Please try again...'))
                    return render(request, 'djauth/addStudent.html', {'first_name': first_name,
                                                        'last_name': last_name,
                                                        'username': username,
                                                        'password': password,
                                                        'grade': grade,
                                                        # 'email': email,
                                                        })
                    
                
                messages.success(request, ('Student has been added to the database!'))
                
                return HttpResponseRedirect("/teacherDash")
            return render(request, 'djauth/addStudent.html', {'form': StudentForm})
        
                
            
            
    
    # otherwise, just return the page bc no info submission
        
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

def teacherExamView(request):
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
        return render(request,'djauth/teacherExamView.html',context)

def addQuestion(request):    
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return HttpResponseRedirect('/confirmation')
        context={'form':form}
        return render(request,'djauth/addQuestion.html',context)

def createExam(request):
    if request.method == 'POST':
        print("request.POST")
        print(request.POST)
        form = ExamForm(request.POST)
        print("form")
        print(form)
        if form.is_valid():
            test = form.save(commit=False)
            test.save()
            
            number_of_questions = int(request.POST.get('number', 1))
            print("number of questions")
            print(number_of_questions)
            # number_of_questions = form.cleaned_data['number']
            QuestionFormSet = formset_factory(addQuestionform, formset=BaseFormSet, extra=number_of_questions)
            
            print("question form set")
            print(QuestionFormSet)
            formset = QuestionFormSet(request.POST, prefix='questions')
            print("formset")
            print(formset)

            if formset.is_valid():
                for question_form in formset.forms:
                    print("question_form")
                    print(question_form)
                    if question_form.is_valid():
                        question = question_form.cleaned_data.get('question')
                        op1 = question_form.cleaned_data.get('op1')
                        op2 = question_form.cleaned_data.get('op2')
                        op3 = question_form.cleaned_data.get('op3')
                        op4 = question_form.cleaned_data.get('op4')
                        ans = question_form.cleaned_data.get('ans')
                        ques_model = QuesModel(question=question, op1=op1, op2=op2, op3=op3, op4=op4, ans=ans)
                        ques_model.save()
                        test.questions.add(ques_model)
                        # question = form.save(commit=False)
                        # question.test = test
                        # question.save()
                        # test.questions.add(question)
                test.save()
        return HttpResponseRedirect('/confirmation')
    else:
        form = ExamForm()
        number_of_questions = int(request.POST.get('number', 1))
        QuestionFormSet = formset_factory(addQuestionform, formset=BaseFormSet, extra=number_of_questions)
        formset = QuestionFormSet(prefix='questions')

    return render(request, 'djauth/createExam.html', {'form': form, 'formset': formset})

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

# def pdfScanner(request):
#     print(request.FILES)
#     if request.method == 'POST' and request.FILES['pdf']:
#         pdf_file = UploadPdfForm(request.POST, request.FILES)
#         fs = FileSystemStorage()
#         filename = fs.save(pdf_file, pdf_file)
#         pdf_url = fs.url(filename)
#         return render(request, 'djauth/pdfScanner.html', {'pdf_url': pdf_url})
#     return render(request, 'djauth/pdfScanner.html')

def dash(request):
    usergroup = None
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

@login_required(login_url="/login")
def fullStudentList(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        students = Student.objects.all()
        usernames = [student.username for student in students]
        print(usernames) 
        return render(request, 'djauth/fullStudentList.html', {'users': students})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
@login_required(login_url="/login")
def edit_student(request, username):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        student = get_object_or_404(Student, username=username)
        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/fullStudentList')
        else:
            form = StudentForm(instance=student)
        context = {'student': student, 'form': form}
        return render(request, 'djauth/edit_student.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
@login_required(login_url="/login")    
def delete_student(request, username):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        student = get_object_or_404(Student, username=username)
        if request.method == 'POST':
            student.delete()
            return HttpResponseRedirect('/fullStudentList')
        return HttpResponseRedirect('/fullStudentList')
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
@login_required(login_url="/login")    
def delete_pdftest(request, pk):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        pdftest = get_object_or_404(PdfTest, pk=pk)
        if request.method == 'POST':
            pdftest.delete()
            return HttpResponseRedirect('/exam_list')
        return HttpResponseRedirect('/exam_list')
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
    
def create_test(request):
    if request.method == 'POST':
        print("AAAAAAAAAAAAAAAAA")
        form = PdfTestForm(request.POST, request.FILES)
        print(request.POST['file_name'])
        print(request.POST['num_questions'])
        if form.is_valid():
            print("BBBBBBBBBBBBBBBB")
            pdf_test = form.save(commit=False)
            pdf_test.pdf = request.FILES['pdf']
            pdf_test.name = request.POST['file_name']
            pdf_test.num_questions = request.POST['num_questions']
            pdf_test.answers =  request.POST['answers']
            pdf_test.save()
            return HttpResponseRedirect("/teacherDash")
        else:
            print(form.errors)
    else:
        form = PdfTestForm()
    
    return render(request, 'djauth/create_test.html', {'form': form})

def take_pdftest(request, pk):
    pdftest = get_object_or_404(PdfTest, pk=pk)
    if request.method == 'POST':
        form = StudentPDFTestForm(pdftest.num_questions, request.POST)
        if form.is_valid():
            student_test = form.save(commit=False)
            student_test.num_questions = request.POST['num_questions']
            student_test.answers =  request.POST['student_answers']
            student_test.save()

            return redirect('pdftest_confirmation', pk=pdftest.pk)  # Redirect to the confirmation page
    else:
        form = StudentPDFTestForm(pdftest.num_questions)
    return render(request, 'djauth/student_pdftest.html', {'pdftest': pdftest, 'form': form})

    

def exam_list(request):
    exams = PdfTest.objects.all()  # Assuming you want to fetch all PdfTest objects
    print(exams)
    context = {'exams': exams}
    return render(request, 'djauth/exam_list.html', context)

def deleteExam(request):
    if request.method == 'POST':
        form = DeleteExamForm(request.POST)
        if form.is_valid():
            test_title = form.cleaned_data['test']
            test = Test.objects.get(title=test_title)
            test.delete()
            return redirect('/confirmation')  # Replace 'confirmation' with the appropriate URL name for the confirmation page
    else:
        form = DeleteExamForm()
    
    return render(request, 'djauth/deleteExam.html', {'form': form})