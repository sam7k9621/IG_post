# Generated by Django 3.2.4 on 2021-06-13 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0005_auto_20210612_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='message',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]