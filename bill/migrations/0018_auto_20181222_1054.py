# Generated by Django 2.1.4 on 2018-12-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0017_auto_20181222_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct',
            name='discount2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='direct',
            name='name2',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='direct',
            name='price2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]