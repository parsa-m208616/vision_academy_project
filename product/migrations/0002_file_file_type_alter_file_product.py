# Generated by Django 5.0.7 on 2024-07-14 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.IntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], default=2),
        ),
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='product.product'),
        ),
    ]
