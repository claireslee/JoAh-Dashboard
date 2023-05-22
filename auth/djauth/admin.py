from django.contrib import admin
from .models import Teacher, Student, QuesModel, Announcement, Test, PdfTest

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(QuesModel)
admin.site.register(Test)
admin.site.register(Announcement)
admin.site.register(PdfTest)



