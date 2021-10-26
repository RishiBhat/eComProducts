# Generated by Django 3.2.8 on 2021-10-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prprice',
            field=models.IntegerField(default=400),
        ),
        migrations.AddField(
            model_name='product',
            name='prqty',
            field=models.IntegerField(default=80),
        ),
        migrations.AddField(
            model_name='product',
            name='prtotal',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='pr',
            field=models.IntegerField(default=400),
        ),
    ]
