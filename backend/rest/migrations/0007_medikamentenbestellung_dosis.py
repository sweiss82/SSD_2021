# Generated by Django 3.2.5 on 2021-07-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_patient_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='medikamentenbestellung',
            name='dosis',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
