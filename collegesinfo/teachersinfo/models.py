from django.db import models
class login(models.Model):
    username: models.TextField(max_length=100)
    password:models.TextField()
    def ___str___(self):
        return self.username

# Create your models here.
