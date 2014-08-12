from django.db import models

# Create your models here.
class Class(models.Model):
    title = models.CharField(max_length=75)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.title



class Student(models.Model):
    klass = models.ForeignKey(Class, related_name="students")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class StudentProject(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey(Student, related_name="project", null=True)

    def __unicode__(self):
        return self.name