# Generated by Django 3.2 on 2021-05-06 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='评论昵称'),
            preserve_default=False,
        ),
    ]
