# Generated by Django 2.1.4 on 2018-12-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0019_auto_20181222_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct',
            name='meters',
            field=models.FloatField(blank=True, null=True),
        ),
    ]