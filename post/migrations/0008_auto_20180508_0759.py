# Generated by Django 2.0.3 on 2018-05-08 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20180508_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
