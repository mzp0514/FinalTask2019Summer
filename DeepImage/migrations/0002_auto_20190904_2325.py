# Generated by Django 2.2.5 on 2019-09-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeepImage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]