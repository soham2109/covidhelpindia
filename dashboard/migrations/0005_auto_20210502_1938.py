# Generated by Django 3.1.6 on 2021-05-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210502_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource_entry',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
