# Generated by Django 3.2.8 on 2021-10-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prname', models.CharField(max_length=500)),
                ('prtype', models.CharField(max_length=500)),
                ('pr', models.CharField(max_length=500)),
            ],
        ),
    ]