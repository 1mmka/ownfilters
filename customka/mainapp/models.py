from django.db import models

# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateTimeField(db_index=True,auto_now_add=False)
    
    def __str__(self):
        return self.name