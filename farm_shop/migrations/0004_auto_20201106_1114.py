# Generated by Django 3.1.2 on 2020-11-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_shop', '0003_itemnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemnews',
            name='label',
            field=models.CharField(default='Заголовок', max_length=100, unique=True),
        ),
    ]
