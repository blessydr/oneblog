# Generated by Django 5.1.1 on 2024-11-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_blog_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='rejection_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]