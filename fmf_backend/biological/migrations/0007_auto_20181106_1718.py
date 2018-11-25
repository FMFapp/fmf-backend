# Generated by Django 2.1.3 on 2018-11-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biological', '0006_auto_20181106_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paineffect',
            name='painType',
            field=models.CharField(blank=True, choices=[('D', 'Dull'), ('S', 'Sharp'), ('B', 'Burning'), ('P', 'Pulling')], max_length=8),
        ),
    ]
