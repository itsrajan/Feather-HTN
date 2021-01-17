# Generated by Django 3.1.5 on 2021-01-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210116_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='admin@local.host', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
