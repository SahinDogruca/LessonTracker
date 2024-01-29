# Generated by Django 3.2.4 on 2021-06-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionTracker', '0003_alter_question_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='questionTracker.subject'),
        ),
    ]
