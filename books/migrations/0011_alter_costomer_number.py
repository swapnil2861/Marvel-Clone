# Generated by Django 3.2.3 on 2021-06-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_costomer_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costomer',
            name='number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
