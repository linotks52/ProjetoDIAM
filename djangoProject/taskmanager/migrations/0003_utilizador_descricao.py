# Generated by Django 4.2.1 on 2023-05-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_utilizador_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizador',
            name='descricao',
            field=models.TextField(default='Ainda sem descricao ,escreva um pouco sobre si!', max_length=300),
        ),
    ]
