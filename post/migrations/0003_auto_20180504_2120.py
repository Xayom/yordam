# Generated by Django 2.0.3 on 2018-05-04 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20180501_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_date',
        ),
        migrations.AddField(
            model_name='article',
            name='Дата публикации',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Автор', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=models.TextField(verbose_name='Заявка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Категория', to='post.Section'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_status',
            field=models.IntegerField(verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
