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
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import PdfTest
from django.db.models import Max
from .forms import PdfTestForm, StudentPDFTestForm
from django.forms import formset_factory
from django.forms import BaseFormSet
from .models import TeacherInquirie
from .forms import TeacherInquirieForm
from django import template
from .forms import DeleteExamForm
from .forms import DeleteQuestionForm
from .forms import EditExamForm


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
from .forms import DeleteExamForm, DeletePDFForm, AddQuestionForm
from .forms import ToDoListForm
from .models import ToDoList
from .models import TeacherInquirie
from .forms import TeacherInquirieForm
from .models import ContactUs
from .forms import ContactUsForm


def mainpage(request):
    
    all_students = Student.objects.all
    return render(request, 'djauth/mainpage.html',{'all':all_students})

def aboutUs(request):
    if request.method == "POST":
        form = TeacherInquirieForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Your message has been submitted!'))
        
        return HttpResponseRedirect("/teacherDash")
        #return render(request, 'teacherAnnouncement.html', {})
        
    else:
        return render(request, 'djauth/aboutUsTab.html')
    
    
@login_required(login_url="/login")
def newTeacher(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        all_teacherinqs = TeacherInquirie.objects.all
        return render(request, 'djauth/newTeacher.html',{'all':all_teacherinqs})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

    
def resources(request):
    return render(request, 'djauth/resources.html')

def calendar(request):
    return render(request, 'djauth/calendar.html')

def programs(request):
    return render(request, 'djauth/programs.html')

def contactus(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Your message has been sent!'))
        
        return HttpResponseRedirect("/teacherDash")
        #return render(request, 'teacherAnnouncement.html', {})
        
    else:
        return render(request, 'djauth/contactus.html')
    
@login_required(login_url="/login")
def newContactUs(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        all_contactus = ContactUs.objects.all
        return render(request, 'djauth/newContactUs.html',{'all':all_contactus})

    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

    

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
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        username = request.user.username
        student = Student.objects.get(username=username)
        
        return render(request, 'studentDashboard/studentDashboard.html')
        

@login_required(login_url="/login") 
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
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        all_students = Student.objects.all
        return render(request, 'djauth/studentDisplay.html',{'all':all_students} )
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    

@login_required(login_url="/login")
def examList(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        tests = Test.objects.all()
        context = {'tests': tests}
        return render(request, 'djauth/examList.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    

@login_required(login_url="/login")
def studentExamList(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        tests = Test.objects.all()
        context = {'tests': tests}
        return render(request, 'studentDashboard/studentExamList.html', context)

@login_required(login_url="/login")
def examDetail(request, test_id):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        test = get_object_or_404(Test, id=test_id)
        questions = test.questions.all()

        if request.method == 'POST':
            question_id = request.POST.get('question')
            question = get_object_or_404(QuesModel, id=question_id)
            test.questions.add(question)  # Add the selected question to the exam
            test.save()

        context = {'test': test, 'questions': questions}
        return render(request, 'djauth/examDetail.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

   

@login_required(login_url="/login")
def studentExamDetail(request, test_id):
    if request.user.is_authenticated:
            usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        if request.method == 'POST':
            print(request.POST)
            test = Test.objects.get(id=test_id)
            questions = test.questions.all()
            score=0
            wrong=0
            correct=0
            total=0
            incorrect_questions = []
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
                    incorrect_questions.append(q)
            percent = score/(total*10) *100
            context = {
                'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total,
                'incorrect_questions':incorrect_questions,
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

def is_pdf(file: UploadedFile) -> bool:
    """
    Check if the uploaded file is a PDF.
    """
    allowed_extensions = ['.pdf']
    return any(file.name.lower().endswith(ext) for ext in allowed_extensions)


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
                    username = form.cleaned_data['username']
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'Username already exists. Please choose a different username.')
                    else:
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
                
                return HttpResponseRedirect("/fullStudentList")
            return render(request, 'djauth/addStudent.html', {'form': StudentForm})
        
                
            
            
    
    # otherwise, just return the page bc no info submission
        
        else:
            return HttpResponseRedirect("/studentDashboard/studentDashboard")
    # if someone posts + fill out form ... 
    
# Create your views here.

@login_required(login_url="/login") 
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

@login_required(login_url="/login") 
def teacherExamView(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
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
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
@login_required(login_url="/login") 
def addQuestion(request):    
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                question = form.cleaned_data['question']
                if QuesModel.objects.filter(question=question).exists():
                    form.add_error('question', ValidationError('A question with this name already exists. Please choose a different name.'))
                else:
                    form.save()
                    return HttpResponseRedirect('/examList')
        context={'form':form}
        return render(request,'djauth/addQuestion.html',context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

        
@login_required(login_url="/login") 
def createExam(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        number_of_questions = 10  # Default value for displaying ten question fields

        if request.method == 'POST':
            form = ExamForm(request.POST)
            if form.is_valid():
                test = form.save(commit=False)
                if Test.objects.filter(title=test.title).exists():
                    form.add_error('title', ValidationError('A test with this name already exists. Please choose a different name.'))
                else:
                    test.save()
                    QuestionFormSet = formset_factory(addQuestionform, formset=BaseFormSet, extra=number_of_questions)
                    formset = QuestionFormSet(request.POST, prefix='questions')

                    for question_form in formset.forms:
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

                    test.save()
                return HttpResponseRedirect('/examList')
        else:
            form = ExamForm()
            QuestionFormSet = formset_factory(addQuestionform, formset=BaseFormSet, extra=number_of_questions)
            formset = QuestionFormSet(prefix='questions')

        return render(request, 'djauth/createExam.html', {'form': form, 'formset': formset, 'number_of_questions': range(number_of_questions)})

    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

@login_required(login_url="/login")     
def deleteExam(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        if request.method == 'POST':
            form = DeleteExamForm(request.POST)
            if form.is_valid():
                test_title = form.cleaned_data['test']
                test = Test.objects.get(title=test_title)
                test.delete()
                return redirect('/examList')  # Replace 'confirmation' with the appropriate URL name for the confirmation page
        else:
            form = DeleteExamForm()
        
        return render(request, 'djauth/deleteExam.html', {'form': form})

    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

@login_required(login_url="/login") 
def addQuestionToExam(request, exam_id):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        test = get_object_or_404(Test, id=exam_id)
    
        # Retrieve all the existing questions
        all_questions = QuesModel.objects.all()
        
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                question_id = form.cleaned_data['question']
                question = get_object_or_404(QuesModel, id=question_id)
                test.questions.add(question)  # Add the question to the test's questions field
                test.save()  # Save the test object
                # Redirect to the exam detail page
                return redirect('/examDetail/' + str(test.id))
        else:
            form = AddQuestionForm()
        
        context = {
            'test': test,
            'form': form,
            'all_questions': all_questions,
        }
        return render(request, 'djauth/addQuestionToExam.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
    
@login_required(login_url="/login") 
def deleteQuestion(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        all_questions = QuesModel.objects.all()
    
        if request.method == 'POST':
            form = DeleteQuestionForm(request.POST)
            if form.is_valid():
                ques = form.cleaned_data['question']
                question = QuesModel.objects.get(question=ques)
                question.delete()
                return redirect('/examList')
        else:
            form = DeleteQuestionForm()
        
        context = {
            'form': form,
            'all_questions': all_questions,
        }
        return render(request, 'djauth/deleteQuestion.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
    
@login_required(login_url="/login") 
def deleteQuestionFromExam(request, exam_id):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        test = get_object_or_404(Test, id=exam_id)
        questions = test.questions.all()  # Get the questions associated with the exam

        if request.method == 'POST':
            form = DeleteQuestionFromExamForm(request.POST, exam_id=exam_id)
            if form.is_valid():
                ques = form.cleaned_data['question']
                question = QuesModel.objects.get(question=ques)
                test.questions.remove(question)  # Remove the question from the test's questions field
                test.save()  # Save the test object
                return redirect('/examDetail/' + str(test.id))
        else:
            form = DeleteQuestionFromExamForm(exam_id=exam_id)

        context = {
            'test': test,
            'questions': questions,
            'form': form,
        }
        return render(request, 'djauth/deleteQuestionFromExam.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

    
@login_required(login_url="/login") 
def editExam(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        if request.method == 'POST':
            form = EditExamForm(request.POST)
            if form.is_valid():
                test = form.cleaned_data['test']
                new_title = form.cleaned_data['title']
                if Test.objects.filter(title=new_title).exists():
                    form.add_error('title', ValidationError('A test with this name already exists. Please choose a different name.'))
                else:
                    test.title = new_title
                    test.save()
                    return redirect('/examList')
        else:
            form = EditExamForm()
        return render(request, 'djauth/editExam.html', {'form': form})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

@login_required(login_url="/login") 
def editQuestion(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        if request.method == 'POST':
            form = EditQuestionForm(request.POST)
            if form.is_valid():
                question = form.cleaned_data['question']
                new_title = form.cleaned_data['questionTitle']
                new_op1 = form.cleaned_data['op1']
                new_op2 = form.cleaned_data['op2']
                new_op3= form.cleaned_data['op3']
                new_op4= form.cleaned_data['op4']
                new_ans = form.cleaned_data['ans']
                if QuesModel.objects.filter(question=new_title).exclude(pk=question.pk).exists():
                    form.add_error('questionTitle', ValidationError('A question with this title already exists. Please choose a different title.'))
                else:
                    question.question = new_title
                    question.op1 = new_op1
                    question.op2 = new_op2
                    question.op3 = new_op3
                    question.op4 = new_op4
                    question.ans = new_ans
                    question.save()
                    return redirect('/examList')
        else:
            form = EditQuestionForm()
        return render(request, 'djauth/editQuestion.html', {'form': form})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

    
@login_required(login_url="/login") 
def confirmation(request):
    if request.user.is_authenticated:
            usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        return HttpResponseRedirect("/confirmation")
    
@login_required(login_url="/login") 
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

@login_required(login_url="/login") 
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


@login_required(login_url="/login")    
def studentAnnouncement(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        all_announcements = Announcement.objects.all
        return render(request, 'studentDashboard/studentAnnouncement.html', {'all_announcements': all_announcements})



@login_required(login_url="/login")     
def teacherAnnouncement(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        if request.method == "POST":
            form = AnnouncementForm(request.POST or None)
            if form.is_valid():
                form.save()
            messages.success(request, ('Your Announcement Has Been Uploaded!'))
            
            return HttpResponseRedirect("/teacherDash")
            #return render(request, 'teacherAnnouncement.html', {})
        
        else:
            return render(request, 'djauth/teacherAnnouncement.html', {})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
@login_required(login_url="/login") 
def create_test(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        if request.method == 'POST':
            form = PdfTestForm(request.POST, request.FILES)
            if form.is_valid():
                name = request.POST['file_name']
                if PdfTest.objects.filter(name=name).exists():
                    form.add_error('file_name', 'A test with this name already exists.')
                else:
                    pdf_test = form.save(commit=False)
                    pdf_test.pdf = request.FILES['pdf']
                    if not is_pdf(pdf_test.pdf):
                        form.add_error('pdf', 'Only PDF files are allowed.')
                        return render(request, 'djauth/create_test.html', {'form': form})
                
                    pdf_test.name = name
                    pdf_test.num_questions = request.POST['num_questions']
                    pdf_test.answers = request.POST['answers']
                    pdf_test.save()
                    return HttpResponseRedirect("/exam_list")
            else:
                print(form.errors)
        else:
            form = PdfTestForm()
        
        return render(request, 'djauth/create_test.html', {'form': form})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    
@login_required(login_url="/login") 
def take_pdftest(request, pk):
    pdftest = get_object_or_404(PdfTest, pk=pk)
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        initial_answers = json.dumps(pdftest.answers)  # Convert dictionary to JSON string

        form = StudentPDFTestForm(pdftest.num_questions, pdftest.answers, initial_answers)
        return render(request, 'djauth/teacher_pdftest.html', {'pdftest': pdftest, 'form': form})

    else:
        
        if request.method == 'POST':
            student_answers = request.POST.getlist('answers')[0] 
            real_answers = json.loads(pdftest.answers)
            form = StudentPDFTestForm(pdftest.num_questions, real_answers, student_answers, request.POST)
           
            if form.is_valid():
                
                student_test = StudentPDFTestForm(pdftest.num_questions, pdftest.answers, student_answers)
                confirmation_url = reverse('studentDashboard/pdftest_confirmation', args=[pdftest.pk])
                confirmation_url += f'?student_answers={student_answers}&real_answers={real_answers}'
                return HttpResponseRedirect(confirmation_url)
                
        else:
            initial_answers = json.dumps(pdftest.answers)  # Convert dictionary to JSON string

            form = StudentPDFTestForm(pdftest.num_questions, pdftest.answers, initial_answers)
        return render(request, 'djauth/student_pdftest.html', {'pdftest': pdftest, 'form': form})

@login_required(login_url="/login") 
def pdftest_confirmation(request, pk):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        pdftest = get_object_or_404(PdfTest, pk=pk)
        student_answers_str = request.GET.get('student_answers', '{}')
        real_answers_str = request.GET.get('real_answers', '{}')

        # Replace single quotes with double quotes in the JSON strings
        student_answers_str = student_answers_str.replace("'", '"')
        real_answers_str = real_answers_str.replace("'", '"')

        # Parse the JSON strings into dictionaries
        student_answers = json.loads(student_answers_str)
        real_answers = json.loads(real_answers_str)

        num_correct = 0
        incorrect_answers = {}

        i=1
        for question_number, student_answer in student_answers.items():
            if student_answer == real_answers.get(question_number):
                num_correct += 1
                i+=1
            else:
                incorrect_answers[i] = {
                    'correct_answer': real_answers.get(question_number),
                    'your_answer': student_answer
                }
                i+=1

        score = num_correct
        percentage = round((score / pdftest.num_questions) * 100, 2)

        


        # Process the student_answers and real_answers as needed
        context = {
            'pdftest': pdftest,
            'real_answers': real_answers,
            'student_answers': student_answers,
            'percentage': percentage,
            'incorrect_answers': incorrect_answers,
        }

        return render(request, 'studentDashboard/pdftest_confirmation.html', context)
        
@login_required(login_url="/login") 
def exam_list(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        exams = PdfTest.objects.all()  # Assuming you want to fetch all PdfTest objects
        context = {'exams': exams}
        return render(request, 'djauth/exam_list.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    

@login_required(login_url="/login")
def studentExam_List(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        exams = PdfTest.objects.all()
        context = {'exams': exams}
        return render(request, 'studentDashboard/studentExam_List.html', context)

@login_required(login_url="/login") 
def addQuestionToExam(request, exam_id):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        test = get_object_or_404(Test, id=exam_id)
# Retrieve all the existing questions
        all_questions = QuesModel.objects.all()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                question_id = form.cleaned_data['question']
                question = get_object_or_404(QuesModel, id=question_id)
                test.questions.add(question) # Add the question to the test's questions field
                test.save() # Save the test object
                # Redirect to the exam detail page
                return redirect('/examDetail/' + str(test.id))
        else:
            form = AddQuestionForm()
        context = {
            'test': test,
            'form': form,
            'all_questions': all_questions,
        }
        return render(request, 'djauth/addQuestionToExam.html', context)
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    


@login_required(login_url="/login") 
def deletePDFExam(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        if request.method == 'POST':
            form = DeletePDFForm(request.POST)
            if form.is_valid():
                test_name = form.cleaned_data['pdftest']
                pdftest = get_object_or_404(PdfTest, name=test_name)
                pdftest.delete()
                return redirect('/confirmation') # Replace 'confirmation' with the appropriate URL name for the confirmation page
        else:
            form = DeletePDFForm()
        
        return render(request, 'djauth/delete_pdftest.html', {'form': form})
    else:
        return HttpResponseRedirect("/studentDashboard/studentDashboard")
    

@login_required(login_url="/login") 
def toDoList(request):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        if request.method == 'POST':
            form = ToDoListForm(request.POST or None)
            
            if form.is_valid():
                form.save()
                all_items = ToDoList.objects.all
                messages.success(request, ('Item has been added to the list'))
                return render(request, 'studentDashboard/studentDashboard.html', {'all_items': all_items})
            
        else:
            all_items = ToDoList.objects.all
            return render(request, 'studentDashboard/studentDashboard.html', {'all_items': all_items})

@login_required(login_url="/login") 
def deleteToDo(request, list_id):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        item = ToDoList.objects.get(pk=list_id)
        item.delete()
        messages.success(request, ('Item has been deleted!'))
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

@login_required(login_url="/login") 
def crossoff(request, list_id):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        item = ToDoList.objects.get(pk=list_id)
        item.completed = True
        item.save()
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

@login_required(login_url="/login") 
def uncross(request, list_id):
    if request.user.is_authenticated:
        usergroup = request.user.groups.values_list('name', flat=True).first()
    if usergroup == "Teacher":
        return HttpResponseRedirect("/teacherDash")
    else:
        item = ToDoList.objects.get(pk=list_id)
        item.completed = False
        item.save()
        return HttpResponseRedirect("/studentDashboard/studentDashboard")

