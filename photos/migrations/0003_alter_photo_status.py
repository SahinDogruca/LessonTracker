# Generated by Django 3.2.6 on 2021-10-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20211028_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='status',
            field=models.CharField(choices=[('False', 'Yanlış'), ('Blank', 'Boş'), ('SSA solved', 'KÇS çözüldü'), ('solved', 'çözüldü'), ('cant solve', 'çözemedim'), ('nice question', 'Güzel soru')], max_length=255, verbose_name='Durum'),
        ),
    ]
