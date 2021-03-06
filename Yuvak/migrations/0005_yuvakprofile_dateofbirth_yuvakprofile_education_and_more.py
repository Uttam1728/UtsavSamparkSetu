# Generated by Django 4.0.1 on 2022-02-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yuvak', '0004_alter_yuvakprofile_area_alter_yuvakprofile_houseno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='yuvakprofile',
            name='DateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='yuvakprofile',
            name='Education',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='yuvakprofile',
            name='Married',
            field=models.BooleanField(default=False),
        ),
    ]
