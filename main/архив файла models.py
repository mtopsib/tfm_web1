from django.db import models


# Create your models here.

### демо таблица - шаблон
# Task - это пробная таблица для примера
class Task(models.Model):
    # Описание полей и свойства полей
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    # эта функция когда мы обращаемся к элементу таблы, определяет что именно мы возвращаем
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


### таблицы 1-ого уровня

# таблица список типов техники бульдозер там самосвал
class tech_type(models.Model):
    techtype = models.CharField('Название типа техники', max_length=120)

    def __str__(self):
        return self.techtype

    class Meta:
        verbose_name = 'Тип техники'
        verbose_name_plural = 'Типы техник'


# TODO УДалиьб??? таблица список видов техники с ценой простоя
class tech_v1(models.Model):
    techmodel = models.CharField('Название модели техники', max_length=120)
    techtype = models.ForeignKey(tech_type, on_delete=models.CASCADE)
    downprice = models.IntegerField('Цена часа простоя')

    def __str__(self):
        return self.techmodel

    class Meta:
        verbose_name = 'Список техники'
        verbose_name_plural = 'Список техник'


# таблица список разрезов
class workarea(models.Model):
    workarea = models.CharField('Название Разреза(учатска)', max_length=120)

    def __str__(self):
        return self.workarea

    class Meta:
        verbose_name = 'Список разрезов (Участков)'
        verbose_name_plural = 'Разрез (Участок)'


# журнал даунтаймов
class downtimejornal1(models.Model):
    techtype = models.ForeignKey(tech_type, on_delete=models.CASCADE)
    region = models.ForeignKey(workarea, on_delete=models.CASCADE)
    garnum = models.CharField('Гаражный номер', max_length=120)
    downdatetime = models.DateTimeField('Время начала простоя')

    # updatetime = models.DateTimeField('Время окончания простоя')

    def __str__(self):
        return "Событие начала простоя: участок %s,  тип техники %s, гаражный номер %s, дата время %s" % (
            self.region, self.techtype, self.garnum, self.downdatetime)

    class Meta:
        verbose_name = 'Журнал начала простоя'
        verbose_name_plural = 'Журнал начала простоев'


# описать таблицу статусов
class GrpStatsDown(models.Model):
    group = models.CharField('Группа простоев', max_length=120)

    def __str__(self):
        return '%s' % (self.group)

    class Meta:
        verbose_name = 'Группа простоя'
        verbose_name_plural = 'Группы простоев'


# TODO описать список ремонтов
class StatDown(models.Model):
    group = models.ForeignKey(GrpStatsDown, on_delete=models.CASCADE)
    kod1c = models.CharField('Код 1с', max_length=120, blank=True)
    name1c = models.CharField('Наименвоание простоя в 1с', max_length=120, blank=True, null=True)
    nameASD = models.CharField('Наименвоание простоя в ASD', max_length=120, blank=True, null=True)
    nameASDlv2 = models.CharField('Наименвоание простоя в ASD', max_length=120, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.nameASD)

    class Meta:
        verbose_name = 'Классификатор простоя'
        verbose_name_plural = 'Классификатор простоев'


# TODO: описать таблицу журнала событий ремонта


class uptimejornal1(models.Model):
    downevent = models.ForeignKey(downtimejornal1, on_delete=models.CASCADE)
    updatetime = models.DateTimeField('Время окончания простоя')

    def __str__(self):
        return "Событие окончание простоя: участок %s,  тип техники %s, гаражный номер %s, c даты время %s по дату %s" % (
            self.downevent.region,
            self.downevent.techtype,
            self.downevent.garnum,
            self.downevent.downdatetime,
            self.updatetime)

    class Meta:
        verbose_name = 'Журнал окончания простоя'
        verbose_name_plural = 'Журнал окончаний простоев'
