# Generated by Django 3.1.2 on 2020-11-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_shop', '0006_auto_20201106_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemnews',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='C:\\Users\\Антон и Юля\\PycharmProjects\\djangoProject\\media'),
        ),
    ]