# Generated by Django 2.1.4 on 2018-12-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0020_auto_20181222_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direct',
            name='name2',
        ),
        migrations.AddField(
            model_name='direct',
            name='meters2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
