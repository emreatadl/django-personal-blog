# Generated by Django 2.2.3 on 2019-10-07 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content2',
        ),
    ]