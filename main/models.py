from django.db import models


# TODO Описать 1.1. Таблица Группа статус простоя (СПР)
class GrpStatDown(models.Model):
    group = models.CharField('Название группы простоев', max_length=120)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Группа статуса простоя'
        verbose_name_plural = '1.1. Группа статусов простов'


# TODO Описать 1.2. Тип техники
class TechType(models.Model):
    tech_type = models.CharField('Название типа техники', max_length=120)

    def __str__(self):
        return self.tech_type

    class Meta:
        verbose_name = 'Тип техники'
        verbose_name_plural = '1.2. Типы техник'


# TODO Описать 1.3. Учсток
class WorkArea(models.Model):
    work_area = models.CharField('Название объекта (Участка)', max_length=120)

    def __str__(self):
        return 'Участок %s' % self.work_area

    class Meta:
        verbose_name = 'Объект (Участок)'
        verbose_name_plural = '1.3. Объекты (Участки)'


# TODO Описать 1.4. Роль тежники
class TechRole(models.Model):
    tech_role = models.CharField('Роль техники', max_length=120)

    def __str__(self):
        return self.tech_role

    class Meta:
        verbose_name = 'Роль техники'
        verbose_name_plural = '1.4. Роли техник'


# TODO Описать 2.1. Справочник Шасси
class Vinechikle(models.Model):
    gar_number = models.CharField('Гаражный номер', max_length=120)
    tech_type = models.ForeignKey(TechType, on_delete=models.CASCADE)
    work_area = models.ForeignKey(WorkArea, on_delete=models.CASCADE)
    tech_role = models.ForeignKey(TechRole, on_delete=models.CASCADE)

    def __str__(self):
        return 'Шасси № %s, тип техники: %s, работает на %s' % (self.gar_number, self.tech_type, self.work_area)

    class Meta:
        verbose_name = 'Шасси'
        verbose_name_plural = '2.1. Шасси'


# TODO Описать 2.2. Справочник Статусы простоев
class StateDown(models.Model):
    grp_stats_down = models.ForeignKey(GrpStatDown, on_delete=models.CASCADE)
    kod_1c = models.CharField('Код простоя в 1с', max_length=120, blank=True, null=True)
    name_1c = models.CharField('Имя простоя в 1с', max_length=120, blank=True, null=True)
    name_ASD = models.CharField('Имя простоя в ASD', max_length=120, blank=True, null=True)
    name_ASDv2 = models.CharField('Имя простоя в ASD level2', max_length=120, blank=True, null=True)
    shot_name = models.CharField('Сокращение простоя', max_length=120, blank=True, null=True)

    def __str__(self):
        return 'Причина простоя код: %s (%s, %s, %s, %s)' % (
        self.pk, self.shot_name, self.name_1c, self.name_ASD, self.name_ASDv2)

    class Meta:
        verbose_name = 'Статус простоя'
        verbose_name_plural = '2.2. Статусы простоя'


# TODO Описать 2.3. Журнал начала простоев
class DownTimeJornal(models.Model):
    vinechikle = models.ForeignKey(Vinechikle, on_delete=models.CASCADE)
    state_down = models.ForeignKey(StateDown, on_delete=models.CASCADE)
    down_date_time = models.DateTimeField('Дата-Время начала простоя')

    def __str__(self):
        return 'Простой № %s, на шасси: %s; начало простоя: %s; причина простоя: %s;' % (
        self.pk, self.vinechikle, self.down_date_time, self.state_down)

    class Meta:
        verbose_name = 'Начало простоя'
        verbose_name_plural = '2.3. Журнал простоев'


# TODO Описать 3.1. Журнал окончаний простов
class UpTimeJornal(models.Model):
    down_time_jornal = models.ForeignKey(DownTimeJornal, on_delete=models.CASCADE)
    up_date_time = models.DateTimeField('Дата-Время окончание простоя')

    def __str__(self):
        return 'Окончание простоя № %s, простой: %s; время окончания простоя: %s' % (
        self.pk, self.down_time_jornal, self.up_date_time)

    class Meta:
        verbose_name = 'Окончание простоя'
        verbose_name_plural = '3.1. Журнал окончаний простоев'
