# Generated by Django 5.1.1 on 2024-09-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
