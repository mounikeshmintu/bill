# Generated by Django 2.1.4 on 2018-12-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0027_direct_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direct',
            name='discount2',
        ),
        migrations.RemoveField(
            model_name='direct',
            name='discount3',
        ),
        migrations.RemoveField(
            model_name='direct',
            name='discount4',
        ),
        migrations.RemoveField(
            model_name='direct',
            name='discount5',
        ),
        migrations.AddField(
            model_name='direct',
            name='grand_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
