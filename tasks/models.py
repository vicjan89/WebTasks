from django.db import models


class Task(models.Model):
    class Repeat(models.IntegerChoices):
        NO_REPEAT = 0, 'Без повтора'
        EVERYDAY = 1, 'Ежедневно'
        EVERYWEEK = 2, 'Еженедельно'
        EVERYMONTH = 3, 'Ежемесячно'
        __empty__ = 'Выберите режим повтора'
    task = models.CharField(max_length=250, verbose_name='Задача')
    start = models.DateTimeField(verbose_name='Начало', null=True, blank=True)
    end = models.DateTimeField(verbose_name='Окончание', null=True, blank=True)
    repeat_mode = models.IntegerField(verbose_name='Режим повторения', null=True, blank=True,
                                      default=Repeat.NO_REPEAT, choices=Repeat.choices)
    priority = models.BooleanField(verbose_name='Важная')
    comment = models.CharField(max_length=250, verbose_name='Комментарий', null=True, blank=True)
    duration = models.FloatField(verbose_name='Трудоёмкость', null=True, blank=True)
    hard = models.BooleanField(verbose_name='Жёсткая')
    progress = models.IntegerField(verbose_name='Прогресс выполнения', null=True, blank=True)
    label = models.ManyToManyField('Label', blank=True, null=True,verbose_name='Метка')
    attachment = models.ManyToManyField('Attachment', blank=True, null=True, verbose_name='Вложение')

    #   child_tasks = List_tasks()

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['start']


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
