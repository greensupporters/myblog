# Generated by Django 2.1 on 2018-09-03 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dest_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
