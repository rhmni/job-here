# Generated by Django 3.2.5 on 2021-07-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_show_for_employers',
            field=models.BooleanField(default=True),
        ),
    ]