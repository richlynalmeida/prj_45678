from django.db import models
from b_wbs.models import Discipline, PmbL03WpExecutionType, PmbL04WpStatusType, PmbL04WpExecutionType


class PMBL03Schedule(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Discipline Code')
    pmb_L03_wp_exe_type = models.ForeignKey(PmbL03WpExecutionType, on_delete=models.CASCADE,
                                            verbose_name='PMB L03 Work Package Execution Type Code', default=1)
    pmb_L03_schedule_code = models.CharField(unique=True, max_length=55, verbose_name='PMB L03 Schedule Code')
    pmb_L03_schedule_title = models.CharField(max_length=2000, blank=True, null=True,
                                              verbose_name='PMB L03 Schedule Title')
    early_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Early Start Date')
    early_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Early Finish Date')
    early_start_to_early_finish_duration = models.IntegerField(blank=True, null=True,
                                                               verbose_name='Early Start to Early Finish Duration')
    late_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Late Start Date')
    late_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Late Finish Date')
    late_start_to_late_finish_duration = models.IntegerField(blank=True, null=True,
                                                             verbose_name='Late Start to Late Finish Duration')
    critical_path_check = models.IntegerField(default=0, verbose_name='Critical Path Check')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='PMB Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 Schedule"
        db_table = 'pmb_L03_schedule'
        app_label = 'h_schedules'
        ordering = ['pmb_L03_schedule_code']

    def __str__(self):
        return f"{self.pmb_L03_schedule_code} - {self.pmb_L03_schedule_title}"


class PMBL04Schedule(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Discipline Code')
    pmb_L04_wp_exe_type = models.ForeignKey(PmbL04WpExecutionType, on_delete=models.CASCADE,
                                            verbose_name='PMB L04 Work Package Execution Type Code', default=1)
    pmb_L03_schedule = models.ForeignKey(PMBL03Schedule, on_delete=models.CASCADE,
                                         verbose_name='PMB L03 Schedule ID')
    pmb_L04_schedule_code = models.CharField(unique=True, max_length=55, verbose_name='PMB L04 Schedule Code')
    pmb_L04_schedule_title = models.CharField(max_length=2000, blank=True, null=True,
                                              verbose_name='PMB L04 Schedule Title')
    early_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Early Start Date')
    early_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Early Finish Date')
    early_start_to_early_finish_duration = models.IntegerField(blank=True, null=True,
                                                               verbose_name='Early Start to Early Finish Duration')
    late_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Late Start Date')
    late_finish_date = models.DateTimeField(blank=True, null=True, verbose_name='Late Finish Date')
    late_start_to_late_finish_duration = models.IntegerField(blank=True, null=True,
                                                             verbose_name='Late Start to Late Finish Duration')
    critical_path_check = models.IntegerField(default=0, verbose_name='Critical Path Check')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='CB Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L04 Schedule"
        db_table = 'pmb_L04_schedule'
        app_label = 'h_schedules'
        ordering = ['pmb_L04_schedule_code']

    def __str__(self):
        return f"{self.pmb_L04_schedule_code} - {self.pmb_L04_schedule_title}"
