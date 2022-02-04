from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=250, verbose_name='Задача')
    start = models.DateTimeField(verbose_name='Начало')
    end = models.DateTimeField(verbose_name='Окончание')
    repeat_mode = models.IntegerField(verbose_name='Режим повторения')
    priority = models.BooleanField(verbose_name='Важная')
    comment = models.CharField(max_length=250, verbose_name='Комментарий')
    duration = models.FloatField(verbose_name='Трудоёмкость')
    hard = models.BooleanField(verbose_name='Жёсткая')
    progress = models.IntegerField(verbose_name='Прогресс выполнения')
    label = models.ForeignKey('Label', null=True, on_delete=models.PROTECT, verbose_name='Метка')
    attachment = models.ForeignKey('Attachment', null=True, on_delete=models.PROTECT, verbose_name='Вложение')

    #   child_tasks = List_tasks()

    def __str__(self):
        return self.task

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-start']


class Attachment(models.Model):
    picture = models.ImageField(verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Вложения'
        verbose_name = 'Вложение'
        ordering = ['picture']

class Label(models.Model):
    label = models.CharField(max_length=30, verbose_name='Метка')

    class Meta:
        verbose_name_plural = 'Метки'
        verbose_name = 'Метка'
        ordering = ['label']

    def __str__(self):
        return self.label
