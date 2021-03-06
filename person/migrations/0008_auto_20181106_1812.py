# Generated by Django 2.1.3 on 2018-11-06 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0007_auto_20181106_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationuse',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='medicationuse',
            name='profile',
        ),
        migrations.AddField(
            model_name='medicationuse',
            name='prespriction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Prescription'),
        ),
        migrations.AlterField(
            model_name='medicationuse',
            name='place_taken',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facilities.Facility'),
        ),
    ]
