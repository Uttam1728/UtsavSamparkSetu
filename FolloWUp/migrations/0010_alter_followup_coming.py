# Generated by Django 4.0.1 on 2022-02-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FolloWUp', '0009_attandance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='Coming',
            field=models.IntegerField(blank=True, choices=[(2, 'Yes'), (3, 'No')], null=True),
        ),
    ]
