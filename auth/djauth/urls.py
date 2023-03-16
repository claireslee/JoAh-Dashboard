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
    path('teacherDash/', views.teacherDash, name="teacherDash.html"),
    path('studentDashboard/studentDashboard/', views.studentDashboard, name="studentDashboard/studentDashboard.html"),
    path('loggedin_view/', views.loggedin_view),
    path('teacherCalendar/', views.teacherCalendar, name="teacherCalendar.html"),
    path('teacherAnnouncement/', views.teacherAnnouncement, name="teacherAnnouncement.html"),
    path('addQuestion/', views.addQuestion, name="addQuestion.html"),
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
    path('confirmation/', views.confirmation ,name='confirmation'),
]