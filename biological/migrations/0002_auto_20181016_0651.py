# Generated by Django 2.1.2 on 2018-10-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biological', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paineffect',
            name='painType',
            field=models.CharField(choices=[('P', 'Pain'), ('I', 'Infections')], max_length=8),
        ),
    ]