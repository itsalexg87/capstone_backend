# Generated by Django 4.2.3 on 2023-07-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
    ]
