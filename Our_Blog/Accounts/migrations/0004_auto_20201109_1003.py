# Generated by Django 3.1.3 on 2020-11-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20200704_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user_model',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
