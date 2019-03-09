# Generated by Django 2.1.7 on 2019-03-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='O mnie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='Awatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='www',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]