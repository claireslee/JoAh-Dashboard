from django.contrib import admin
from .models import Teacher, Student, QuesModel, Announcement

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(QuesModel)
admin.site.register(Announcement)


