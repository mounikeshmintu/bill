# Generated by Django 2.1.4 on 2018-12-19 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0012_auto_20181219_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rate2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='total2',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='bill.Category'),
        ),
    ]