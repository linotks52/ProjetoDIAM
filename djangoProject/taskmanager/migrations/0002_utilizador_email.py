# Generated by Django 4.2.1 on 2023-05-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizador',
            name='email',
            field=models.CharField(default='indefinido', max_length=200),
            preserve_default=False,
        ),
    ]
