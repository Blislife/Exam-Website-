from django.db import models

# Create your models here.
class studentNames(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)

    def __str__(self):
        return self.firstName, self.lastName