# Generated by Django 3.2.5 on 2021-07-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medikamentenbestellung',
            name='medikamentenname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='medikamentenbestellung',
            name='menge',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medikamentenbestellung',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]