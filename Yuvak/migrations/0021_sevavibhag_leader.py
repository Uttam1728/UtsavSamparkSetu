# Generated by Django 3.2.12 on 2022-04-07 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Yuvak', '0020_sevavibhag_yuvaks'),
    ]

    operations = [
        migrations.AddField(
            model_name='sevavibhag',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seva_leader', to='Yuvak.yuvakprofile'),
        ),
    ]
