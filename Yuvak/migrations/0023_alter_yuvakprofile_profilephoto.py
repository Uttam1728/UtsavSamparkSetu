# Generated by Django 3.2 on 2023-04-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yuvak', '0022_yuvakprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yuvakprofile',
            name='ProfilePhoto',
            field=models.ImageField(blank=True, null=True, upload_to='media/yuvak'),
        ),
    ]
