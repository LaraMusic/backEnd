# Generated by Django 3.1.1 on 2020-10-20 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laramusicAPI', '0002_auto_20201019_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musiclist',
            old_name='TypeList',
            new_name='type_list',
        ),
        migrations.AddField(
            model_name='album',
            name='album_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='musictrack',
            name='song_year',
            field=models.PositiveIntegerField(default=0),
        ),
    ]