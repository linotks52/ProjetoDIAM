# Generated by Django 4.2.1 on 2023-05-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0011_alter_utilizador_descricao_alter_utilizador_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='descricao',
            field=models.TextField(default='Ainda sem descricao, escreva um pouco sobre si!', max_length=300),
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]