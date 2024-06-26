# Generated by Django 5.0 on 2024-03-23 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MemeIOX', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_file',
            field=models.ImageField(default='https://placehold.co/500x500', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MemeIOX.topic'),
        ),
    ]
