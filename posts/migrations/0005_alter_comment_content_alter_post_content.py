# Generated by Django 4.2.1 on 2023-05-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, verbose_name='내용'),
        ),
    ]
