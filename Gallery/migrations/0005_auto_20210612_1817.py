# Generated by Django 3.2.4 on 2021-06-12 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_auto_20210612_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottery',
            name='hash_text',
        ),
        migrations.RemoveField(
            model_name='lottery',
            name='pic_pos',
        ),
        migrations.RemoveField(
            model_name='lottery',
            name='pic_url',
        ),
        migrations.RemoveField(
            model_name='lottery',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='lottery',
            name='tag_text',
        ),
        migrations.AddField(
            model_name='lottery',
            name='content',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lottery',
            name='follow_account',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lottery',
            name='url',
            field=models.URLField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lottery',
            name='url_pic',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]