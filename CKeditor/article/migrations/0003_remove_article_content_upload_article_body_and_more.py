# Generated by Django 4.0.1 on 2022-01-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_content_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content_upload',
        ),
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
