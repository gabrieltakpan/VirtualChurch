# Generated by Django 5.1.5 on 2025-03-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_sermon_delete_videolibrary'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sermon_images/'),
        ),
    ]
