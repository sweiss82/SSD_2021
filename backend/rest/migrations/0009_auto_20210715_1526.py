# Generated by Django 3.2.5 on 2021-07-15 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0008_auto_20210715_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apotheke',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=255, null=True)),
                ('strasse', models.CharField(max_length=255, null=True)),
                ('nr', models.CharField(max_length=10, null=True)),
                ('plz', models.CharField(max_length=10, null=True)),
                ('ort', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='medikamentenbestellung',
            name='apotheke',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.apotheke'),
        ),
    ]
