# Generated by Django 3.1.1 on 2020-11-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_profile_second_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='C:\\\\Users\\\\Jayit\\\\Downloads\\\\PharmaCat\\\\DJANGO\\\\minor\\\\website\\\\images\\\\avtar.png', upload_to='website/images'),
        ),
    ]
