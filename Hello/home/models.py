from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=122)
    desc= models.TextField()
    date= models.DateField()

    #when you make migration with this -- it will show No changes detected. -- SO HAVE TO TAKE CARE OF TWO THINGS FIRST..
        #1. Register your model first in admin
        #2. Copy the Name from the Apps and go to settings And paste it in the Installed APP home.apps.HomeConfig
    #the below function will return the name of the same that will display in the admin of Django  instead of Contact Object name it will show the name of the field.
    def __str__(self) -> str:
        return self.name       