from django.db import models

# Create your models here.
class students(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    is_faculty = models.BooleanField(False)

    def __str__(self):
        return self.firstName, self.lastName, self.email, self.username, self.password

class Item(models.Model):
    studentUsers = models.ForeignKey(students, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.text

class faculty(students):
    FirstName = models.CharField(max_length=80)
    LastName = models.CharField(max_length=80)
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=80)
    Password = models.CharField(max_length=80)
    Is_faculty = models.BooleanField(True)
    permissions = [("check_reports")]