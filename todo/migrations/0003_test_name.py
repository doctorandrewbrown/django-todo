# Generated by Django 3.2.23 on 2024-01-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
