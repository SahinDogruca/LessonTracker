# Generated by Django 3.1.5 on 2021-06-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeTracker', '0005_alter_time_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
