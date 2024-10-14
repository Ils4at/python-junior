from django.db import models
from django.db.models import Manager


class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """
    def get_queryset(self):
        """
        Переопределенный кверисет с фильтрацией сотрудников с заданной датой принятия на работу и с не пустым табельным номером отличным от 0
        """
        return super().get_queryser().filter(startwork_date__isnull=False, tab_num__qt=0)

    def get_workers_info(self):
        """
            Получение списка строк в которых содержится
        фамилия, имя, табельный номер сотрудника а также название подразделения в котором числится
        Строки упорядочены по фамилии и имени сотрудника.
        Каждая строка должна быть в формате вида: Васильев Василий, 888, Подразделение №1
        """
        result = Worker.objects.get_queryset().select_related("department")
        list_staff = []
        for item in result:
            list_staff.append(' '.join([item.first_name, item.last_name]))
            list_staff.append(item.tab_num)
            list_staff.append(item.department)
        return list_staff
        # raise NotImplementedError


class Department(models.Model):
    objects = Manager()
    name = models.CharField('Наименование', max_length=30)

    @property
    def get_active_worker_count(self):
        """
        Количество активных сотрудников подразделения
        """
        return Worker.objects.all().select_related("department").filter(department=self.pk).count()
        # raise NotImplementedError

    @property
    def get_all_worker_count(self):
        """
        Количество всех сотрудников подразделения
        """

        return Worker.objects_all.all().select_related("department").filter(department=self.pk).count()
        # raise NotImplementedError

    class Meta:
        db_table = 'department'


class Worker(models.Model):
    """
    Сотрудник
    """

    objects = WorkerManager()
    objects_all = Manager()

    first_name = models.CharField('Фамилия', max_length=30)
    last_name = models.CharField('Имя', max_length=30)
    startwork_date = models.DateField('Дата выхода на работу', null=True, )
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'workers'
        verbose_name = 'Сотрудник'

