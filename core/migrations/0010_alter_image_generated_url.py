# Generated by Django 4.0.4 on 2022-05-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_image_generated_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='generated_url',
            field=models.CharField(default='', max_length=250),
        ),
    ]
