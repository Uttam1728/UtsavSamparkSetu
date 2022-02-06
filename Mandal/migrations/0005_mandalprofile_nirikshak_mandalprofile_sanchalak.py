# Generated by Django 4.0.1 on 2022-02-06 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Yuvak', '0002_yuvakprofile_mandal'),
        ('Mandal', '0004_alter_karyakram_mandal'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandalprofile',
            name='Nirikshak',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nirikshak', to='Yuvak.yuvakprofile'),
        ),
        migrations.AddField(
            model_name='mandalprofile',
            name='Sanchalak',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sanchalak', to='Yuvak.yuvakprofile'),
        ),
    ]