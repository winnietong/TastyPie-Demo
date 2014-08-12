from django.contrib import admin
from models import Student, Class, StudentProject

# Register your models here.
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(StudentProject)