# Generated by Django 3.2.4 on 2021-06-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0002_lottery_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]