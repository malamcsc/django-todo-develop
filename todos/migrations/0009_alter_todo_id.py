# Generated by Django 4.2 on 2023-04-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_auto_20191202_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]