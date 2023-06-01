"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.mainpage, name="mainpage.html"),
    path('mainpage/', views.mainpage, name="mainpage.html"),
    path('aboutUs/', views.aboutUs, name="aboutUsTab.html"),
    path('resources/', views.resources, name="resources.html"),
    path('calendar/', views.calendar, name="calendar.html"),
    path('programs/', views.programs, name="programs.html"),
    path('contactus/', views.contactus, name="contactus.html"),
    path('newContactUs/', views.newContactUs ,name='newContactUs.html'),
    path('teacherDash/', views.teacherDash, name="teacherDash.html"),
    # path('studentDashboard/studentDashboard/', views.studentDashboard, name="studentDashboard/studentDashboard.html"),
    path('loggedin_view/', views.loggedin_view),
    path('teacherCalendar/', views.teacherCalendar, name="teacherCalendar.html"),
    path('teacherAnnouncement/', views.teacherAnnouncement, name="teacherAnnouncement.html"),
    path('addQuestion/', views.addQuestion, name="addQuestion.html"),
    path('examList/', views.examList, name="examList.html"),
    path('studentDashboard/studentCalendar/', views.studentCalendar, name="studentDashboard/studentCalendar.html"),
    path('studentDashboard/studentAnnouncement/', views.studentAnnouncement, name="studentDashboard/studentAnnouncement.html"),
    path('studentDashboard/startExam/', views.startExam, name="studentDashboard/startExam.html"),
    path('dash/', views.dash, name="dash"),
    path('acttestprep/', views.acttestprep, name="acttestprep.html"),
    path('algebra1/', views.algebra1, name="algebra1.html"),
    path('apcalc/', views.apcalc, name="apcalc.html"),
    path('aphistory/', views.aphistory, name="aphistory.html"),
    path('aplang/', views.aplang, name="aplang.html"),
    path('geometry/', views.geometry, name="geometry.html"),
    path('jr1/', views.jr1, name="jr1.html"),
    path('jr2/', views.jr2, name="jr2.html"),
    path('jr3/', views.jr3, name="jr3.html"),
    path('satadvanced/', views.satadvanced, name="satadvanced.html"),    
    path('satbasic/', views.satbasic, name="satbasic.html"),
    path('sattestprep/', views.sattestprep, name="sattestprep.html"),
    path('tutor/', views.tutor, name="tutor.html"),
    path('addStudent/', views.addStudent, name="addStudent.html"),
    path('studentDisplay/', views.studentDisplay, name="studentDisplay.html"),
    path('studentDashboard/home/', views.home ,name='studentDashboard/home.html'),
    path('studentDashboard/result/', views.result ,name='studentDashboard/result.html'),
    path('confirmation/', views.confirmation ,name='confirmation.html'),
    path('teacherExamView/', views.teacherExamView, name="teacherExamView.html"),
    path('createExam/', views.createExam, name="createExam.html"),
    path('deleteExam/', views.deleteExam, name="deleteExam.html"),
    path('deleteQuestion/', views.deleteQuestion, name="deleteQuestion.html"),
    path('deleteQuestionFromExam/<int:exam_id>/', views.deleteQuestionFromExam, name='deleteQuestionFromExam.html'),
    path('examList/', views.examList, name='examList'),
    path('studentDashboard/studentExamList/', views.studentExamList, name='studentExamList'),
    path('examDetail/<int:test_id>/', views.examDetail, name='examDetail'),
    path('studentDashboard/studentExamDetail/<int:test_id>/', views.studentExamDetail, name='studentDashboard/studentExamDetail'),
    path('fullStudentList/', views.fullStudentList, name='fullStudentList'),
    path('edit_student/<str:username>/', views.edit_student, name='edit_student'),
    path('delete_student/<str:username>/', views.delete_student, name='delete_student'),
    path('create_test/', views.create_test, name='create_test'),
    path('pdftest/<int:pk>/', views.take_pdftest, name='take_pdftest'),
    path('addQuestionToExam/<int:exam_id>/', views.addQuestionToExam, name='addQuestionToExam'),
    path('editExam/', views.editExam, name="editExam.html"),
    path('editQuestion/', views.editQuestion, name="editQuestion.html"),
    path('deletePDFExam', views.deletePDFExam, name="delete_pdftest.html"),
    path('addQuestionToExam/<int:exam_id>/', views.addQuestionToExam, name='addQuestionToExam'),
    # path('delete_pdftest/<int:pk>/', views.delete_pdftest, name='delete_pdftest'),
    path('newTeacher/', views.newTeacher ,name='newTeacher.html'),
    path('exam_list/', views.exam_list, name='exam_list'),
    path('studentDashboard/studentExam_List/', views.studentExam_List, name='studentDashboard/studentExam_List'),
    path('studentDashboard/pdftest_confirmation/<int:pk>/', views.pdftest_confirmation, name='studentDashboard/pdftest_confirmation'),

    path('studentDashboard/studentDashboard/', views.toDoList, name='toDoList.html'),
    path('deleteToDo/<int:list_id>', views.deleteToDo, name='deleteToDo'),
    path('crossoff/<int:list_id>', views.crossoff, name='crossoff'),
    path('uncross/<int:list_id>', views.uncross, name='uncross'),
]