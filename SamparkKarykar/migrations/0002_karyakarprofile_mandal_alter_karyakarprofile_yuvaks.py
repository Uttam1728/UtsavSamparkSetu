# Generated by Django 4.0.1 on 2022-02-03 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mandal', '0001_initial'),
        ('Yuvak', '0002_yuvakprofile_mandal'),
        ('SamparkKarykar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyakarprofile',
            name='mandal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mandal.mandalprofile'),
        ),
        migrations.AlterField(
            model_name='karyakarprofile',
            name='Yuvaks',
            field=models.ManyToManyField(blank=True, to='Yuvak.YuvakProfile'),
        ),
    ]