# Generated by Django 2.1.4 on 2018-12-19 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0013_auto_20181219_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name2',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rate2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='total2',
            field=models.IntegerField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bill.Category'),
        ),
    ]