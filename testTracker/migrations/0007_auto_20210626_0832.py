# Generated by Django 3.1.5 on 2021-06-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testTracker', '0006_auto_20210625_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areatest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='branchtest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
