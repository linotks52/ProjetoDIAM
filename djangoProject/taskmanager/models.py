from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('pouca', 'Pouca'),
        ('mediana', 'Mediana'),
        ('alta', 'Alta')
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
    imagem = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    descricao = models.TextField( default ="Ainda sem descricao ,escreva um pouco sobre si!")

    datadecriacao = models.DateField(auto_now_add=True)

    def tarefascriadas(self):
        return Task.objects.filter(user=self.user).count()

    def tarefasadecorrer(self):
        return Task.objects.filter(user=self.user,completed=False).count()

    def tarefasconcluidas(self):
        return Task.objects.filter(user=self.user, completed=True).count()

    def __str__(self):
        return f'{self.user.username} Utilizador'

    isAdmin = models.BooleanField(default=False)

