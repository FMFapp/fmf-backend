# Generated by Django 2.1.3 on 2018-11-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0004_auto_20181106_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='mutation',
            name='note',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
