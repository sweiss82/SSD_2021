# Generated by Django 3.2.5 on 2021-07-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IAM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
