# Generated by Django 3.1.6 on 2021-05-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210502_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource_entry',
            name='resource',
            field=models.CharField(choices=[('Hospital', 'Hospital'), ('Oxygen', 'Oxygen'), ('Remedesvir', 'Remedesvir'), ('Ambulance', 'Ambulance'), ('Plasma', 'Plasma'), ('Other_meds', 'Other_meds'), ('Others', 'Others')], default='Others', max_length=20),
        ),
    ]
