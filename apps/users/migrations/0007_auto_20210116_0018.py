# Generated by Django 3.1.5 on 2021-01-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(to='users.Interest'),
        ),
    ]
