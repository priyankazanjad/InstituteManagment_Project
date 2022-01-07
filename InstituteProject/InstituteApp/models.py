from django.db import models

class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True,auto_created=True)
    dept_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.dept_id},{self.dept_name}"

class Professor(models.Model):
    prof_id = models.ManyToManyField(Department)
    prof_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.prof_id},{self.prof_name},{self.subject}"

class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.rollno},{self.name},{self.marks}"


# Create your models here.
