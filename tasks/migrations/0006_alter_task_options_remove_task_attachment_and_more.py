# Generated by Django 4.0.2 on 2022-02-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_attachment_alter_task_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['start'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='attachment',
        ),
        migrations.AddField(
            model_name='task',
            name='attachment',
            field=models.ManyToManyField(blank=True, null=True, to='tasks.Attachment', verbose_name='Вложение'),
        ),
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(blank=True, null=True, to='tasks.Label', verbose_name='Метка'),
        ),
    ]
