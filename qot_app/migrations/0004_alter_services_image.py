# Generated by Django 5.0 on 2024-06-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qot_app', '0003_alter_services_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]