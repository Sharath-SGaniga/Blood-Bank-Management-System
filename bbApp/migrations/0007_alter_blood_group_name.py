# Generated by Django 4.0.3 on 2024-03-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbApp', '0006_request_physician_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_group',
            name='name',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=250),
        ),
    ]