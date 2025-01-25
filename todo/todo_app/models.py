from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
 


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    isDone = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
    