# Generated by Django 3.1.6 on 2021-05-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource_entry',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
