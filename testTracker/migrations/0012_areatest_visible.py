# Generated by Django 4.0.2 on 2022-04-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testTracker', '0011_alter_areatest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='areatest',
            name='visible',
            field=models.BooleanField(blank=True, null=True, verbose_name='Görünürlük'),
        ),
    ]
