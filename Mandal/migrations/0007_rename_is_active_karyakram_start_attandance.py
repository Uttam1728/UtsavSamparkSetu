# Generated by Django 4.0.1 on 2022-02-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mandal', '0006_rename_for_all_karyakram_start_folloup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karyakram',
            old_name='is_active',
            new_name='Start_Attandance',
        ),
    ]
