# Generated by Django 2.1.4 on 2018-12-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0021_auto_20181222_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct',
            name='meters',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='direct',
            name='meters2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]