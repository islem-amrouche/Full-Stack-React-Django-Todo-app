from django.db import models

# Create your models here.
class Todo(models.Model):
   content        =models.CharField(max_length=255)
   checked        =models.BooleanField(default=False, null=True)
   date_created   =models.DateTimeField(auto_now_add=True, null=True)

   def __str__(self):
     return self.content

