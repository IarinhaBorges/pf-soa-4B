from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(_max_length=254)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    UserId = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    completed = models.BooleanField
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.CharField(max_length=100)
    ano = models.IntegerField()
    def __str__(self):
        return self.name

class Todo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    segundos = models.IntegerField()
    def __str__(self):
        return self.name