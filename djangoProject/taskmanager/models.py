from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Utilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    imagem = models.CharField(max_length=100, default='taskmanager/images/default-user-image.png')
    descricao = models.TextField(max_length=300, default ="Ainda sem descricao ,escreva um pouco sobre si!")
    tarefascriadas = models.IntegerField(default=0)
    tarefasconcluidas = models.IntegerField(default=0)
    datadecriacao = models.DateField(auto_now_add=True)