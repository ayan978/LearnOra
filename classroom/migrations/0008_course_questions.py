# Generated by Django 3.2 on 2021-05-06 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
        ('classroom', '0007_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='questions',
            field=models.ManyToManyField(to='question.Question'),
        ),
    ]
