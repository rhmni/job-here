# Generated by Django 3.2.5 on 2021-07-15 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_employer',
            new_name='is_company',
        ),
    ]