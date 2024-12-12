from django.db import models

# Create your models here.
class user(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        STUDENT = "STUDENT", 'Student'
        FACULTY = "FACULTY", 'Faculty'

    base_role = Role.FACULTY

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    #def __str__(self):
        #return self.firstName, self.lastName, self.email, self.username, self.password

class student(user):
    base_role = user.Role.STUDENT

    class Meta:
        proxy = True
    