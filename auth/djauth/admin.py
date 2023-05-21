from django.contrib import admin
from .models import Teacher, Student, QuesModel, Announcement, Test

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(QuesModel)
admin.site.register(Test)
admin.site.register(Announcement)


