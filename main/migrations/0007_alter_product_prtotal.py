# Generated by Django 3.2.8 on 2021-10-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211027_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prtotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]