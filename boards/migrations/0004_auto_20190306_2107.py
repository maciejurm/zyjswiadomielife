# Generated by Django 2.1.7 on 2019-03-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20190305_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('thumbnail_url', models.URLField(max_length=255)),
                ('html', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='board',
            name='body',
            field=models.TextField(verbose_name='Opis kategorii'),
        ),
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(upload_to='board-cover', verbose_name='Tło kategorii'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='embed',
            field=models.URLField(blank=True, help_text='W tym polu możesz dodać link do dowolnej treści spoza żyj świadomie. Może to być blog, wideo lub cokolwiek innego. Nie musisz opisywać linku, zostanie to zrobione na podstawie treści w linku.', max_length=255, null=True, verbose_name='Załącz treści'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Tytuł'),
        ),
    ]