# Generated by Django 4.2.1 on 2023-05-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_utilizador_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='imagem',
            field=models.CharField(default='taskmanager/images/default-user-image.png', max_length=100),
        ),
    ]
