# Generated by Django 3.1.2 on 2020-11-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_shop', '0007_auto_20201106_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemnews',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='item_news/'),
        ),
    ]
