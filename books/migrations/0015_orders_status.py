# Generated by Django 3.2.3 on 2021-07-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20210704_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
