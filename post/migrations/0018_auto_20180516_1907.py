# Generated by Django 2.0.3 on 2018-05-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20180515_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_photo',
            field=models.ImageField(upload_to='photo', verbose_name='Фото'),
        ),
    ]
