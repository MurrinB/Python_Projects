# Generated by Django 3.1.7 on 2021-03-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210328_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
