# Generated by Django 2.1.7 on 2019-03-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_auto_20190308_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='subscribe',
            field=models.BooleanField(default=False),
        ),
    ]
