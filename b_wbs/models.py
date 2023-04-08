from django.db import models


class WBSType(models.Model):
    wbs_type_code = models.CharField(unique=True, max_length=5, verbose_name='WBS Type Code')
    wbs_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                      verbose_name='WBS Type Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "WBS Types"
        db_table = 'wbs_type'
        app_label = 'b_wbs'
        ordering = ['wbs_type_code']

    def __str__(self):
        return f"{self.wbs_type_code} - {self.wbs_type_title}"


class WBS(models.Model):
    wbs_type = models.ForeignKey(WBSType, on_delete=models.CASCADE, verbose_name='WBS Type ID', default=1)
    wbs_code = models.CharField(unique=True, max_length=5, verbose_name='WBS Code')
    wbs_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                 verbose_name='WBS Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "WBS"
        db_table = 'wbs'
        app_label = 'b_wbs'
        ordering = ['wbs_code']
        unique_together = ['wbs_type', 'wbs_code']

    def __str__(self):
        return f"{self.wbs_code} - {self.wbs_title}"


class PmbL03WpExecutionType(models.Model):
    pmb_L03_wp_exe_type_code = models.CharField(unique=True, max_length=5, verbose_name='PMB L03 Execution Type Code')
    pmb_L03_wp_exe_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                                 verbose_name='PMB L03 WP Execution Type Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 Work Package Execution Types"
        db_table = 'pmb_L03_wp_exe_type'
        app_label = 'b_wbs'
        ordering = ['pmb_L03_wp_exe_type_code']

    def __str__(self):
        return f"{self.pmb_L03_wp_exe_type_code} - {self.pmb_L03_wp_exe_type_title}"


class PmbL04WpExecutionType(models.Model):
    pmb_L03_wp_exe_type = models.ForeignKey(PmbL03WpExecutionType, on_delete=models.CASCADE,
                                            verbose_name='PMB L03 WP Execution Type ID', default=1)
    pmb_L04_wp_exe_type_code = models.CharField(unique=True, max_length=5,
                                                verbose_name='PMB L04 WP Execution Type Code')
    pmb_L04_wp_exe_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                                 verbose_name='PMB L04 WP Execution Type Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L04 Work Package Execution Types"
        db_table = 'pmb_L04_wp_exe_type'
        app_label = 'b_wbs'
        ordering = ['pmb_L04_wp_exe_type_code']

    def __str__(self):
        return f"{self.pmb_L04_wp_exe_type_code} - {self.pmb_L04_wp_exe_type_title}"


class PmbL03WpStatusType(models.Model):
    pmb_L03_wp_status_code = models.CharField(unique=True, max_length=5, verbose_name='PMB L03 WP Status Code')
    pmb_L03_wp_status_title = models.CharField(unique=True, max_length=55, verbose_name='PMB L03 WP Status Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 WP Status Types"
        db_table = 'pmb_L03_wp_status_type'
        app_label = 'b_wbs'
        ordering = ['pmb_L03_wp_status_code']

    def __str__(self):
        return f"{self.pmb_L03_wp_status_code} - {self.pmb_L03_wp_status_title}"


class PmbL04WpStatusType(models.Model):
    pmb_L04_wp_status_code = models.CharField(unique=True, max_length=5, verbose_name='PMB L04 WP Status Code')
    pmb_L04_wp_status_title = models.CharField(unique=True, max_length=55, verbose_name='PMB L04 WP Status Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L04 WP Status Types"
        db_table = 'pmb_L04_wp_status_type'
        app_label = 'b_wbs'
        ordering = ['pmb_L04_wp_status_code']

    def __str__(self):
        return f"{self.pmb_L04_wp_status_code} - {self.pmb_L04_wp_status_title}"


class Department(models.Model):
    department_code = models.CharField(unique=True, max_length=5, verbose_name='Department Code', )
    department_title = models.CharField(unique=True, max_length=55, verbose_name='Department Title', )
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Departments"
        db_table = 'department'
        app_label = 'b_wbs'
        ordering = ['department_code']

    # def __str__(self):
    #     return str('%s' % self.department_code)
    def __str__(self):
        return f"{self.department_code} - {self.department_title}"


class Discipline(models.Model):
    discipline_code = models.CharField(unique=True, max_length=5, verbose_name='Discipline Code')
    discipline_title = models.CharField(unique=True, max_length=55, verbose_name='Discipline Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Disciplines"
        db_table = 'discipline'
        app_label = 'b_wbs'
        ordering = ['discipline_code']

    # def __str__(self):
    #     return str('%s' % self.discipline_code)
    def __str__(self):
        return f"{self.discipline_code} - {self.discipline_title}"


class CostTypeClass(models.Model):
    cost_type_class_code = models.CharField(unique=True, max_length=10, verbose_name='Cost Type Class Code')
    cost_type_class_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                             verbose_name='Cost Type Class Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Cost Type Classes"
        db_table = 'cost_type_class'
        app_label = 'b_wbs'
        ordering = ['cost_type_class_code']

    # def __str__(self):
    #     return str('%s' % self.cost_type_class_code)
    def __str__(self):
        return f"{self.cost_type_class_code} - {self.cost_type_class_title}"


class CostType(models.Model):
    cost_type_class = models.ForeignKey(CostTypeClass, on_delete=models.CASCADE, verbose_name='Cost Type Class ID',
                                        default=1)
    cost_type_code = models.CharField(unique=True, max_length=20, verbose_name='Cost Type Code')
    cost_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                       verbose_name='Cost Type Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Cost Types"
        db_table = 'cost_type'
        app_label = 'b_wbs'
        ordering = ['cost_type_code']

    # def __str__(self):
    #     return str('%s' % self.cost_type_code)
    def __str__(self):
        return f"{self.cost_type_code} - {self.cost_type_title}"


class FacilitySystem(models.Model):
    facility_system_code = models.CharField(unique=True, max_length=5, verbose_name='Facility System Code')
    facility_system_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                             verbose_name='Facility System Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Facility Systems"
        db_table = 'facility_system'
        app_label = 'b_wbs'
        ordering = ['facility_system_code']

    # def __str__(self):
    #     return str('%s' % self.facility_system_code)
    def __str__(self):
        return f"{self.facility_system_code} - {self.facility_system_title}"


class FacilitySystemDetail(models.Model):
    facility_system = models.ForeignKey(FacilitySystem, on_delete=models.CASCADE, verbose_name='Facility System ID')
    facility_system_detail_code = models.CharField(unique=True, max_length=15,
                                                   verbose_name='Facility System Detail Code')
    facility_system_detail_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                                    verbose_name='Facility System Detail Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Facility System Details"
        db_table = 'facility_system_detail'
        app_label = 'b_wbs'
        ordering = ['facility_system_detail_code']
        unique_together = [['facility_system', 'facility_system_detail_code']]

    # def __str__(self):
    #     return str('%s' % self.facility_system_detail_code)
    def __str__(self):
        return f"{self.facility_system_detail_code} - {self.facility_system_detail_title}"

# class TABType(models.Model):
#     tab_type_code = models.CharField(unique=True, max_length=5, verbose_name='TAB Type Code')
#     tab_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
#                                        verbose_name='TAB Type Title')
#     comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='TAB Type Comments')
#
#     class Meta:
#         managed = True
#         verbose_name_plural = "TAB Types"
#         db_table = 'tab_type'
#         app_label = 'b_wbs'
#         ordering = ['tab_type_code']
#
#     def __str__(self):
#         return f"{self.tab_type_code} - {self.tab_type_title}"


# class TABStatus(models.Model):
#     tab_status_code = models.CharField(unique=True, max_length=5, verbose_name='TAB Status Code')
#     tab_status_title = models.CharField(unique=True, max_length=55, verbose_name='TAB Status Title')
#     comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='TAB Status Comments')
#
#     class Meta:
#         managed = True
#         verbose_name_plural = "EB Work Package Statuses"
#         db_table = 'tab_status'
#         app_label = 'b_wbs'
#         ordering = ['tab_status_code']
#
#     def __str__(self):
#         return f"{self.tab_status_code} - {self.tab_status_title}"


# class PMBType(models.Model):
#     tab_type = models.ForeignKey(TABType, on_delete=models.CASCADE, verbose_name='TAB Type ID')
#     pmb_type_code = models.CharField(unique=True, max_length=5, verbose_name='PMB Type Code')
#     pmb_type_title = models.CharField(unique=True, max_length=55, verbose_name='PMB Type Title')
#     comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='PMB Type Comments')
#
#     class Meta:
#         managed = True
#         verbose_name_plural = "PMB Types"
#         db_table = 'pmb_type'
#         app_label = 'b_wbs'
#         ordering = ['pmb_type_code']

# def __str__(self):
#     return f"{self.pmb_type_code} - {self.pmb_type_title}"


# class PMBStatus(models.Model):
#     pmb_status_code = models.CharField(unique=True, max_length=5, verbose_name='PMB Status Code')
#     pmb_status_title = models.CharField(unique=True, max_length=55, verbose_name='PMB Status Title')
#     comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='PMB Status Comments')
#
#     class Meta:
#         managed = True
#         verbose_name_plural = "CB Work Package Statuses"
#         db_table = 'pmb_status'
#         app_label = 'b_wbs'
#         ordering = ['pmb_status_code']
#
#     def __str__(self):
#         return f"{self.pmb_status_code} - {self.pmb_status_title}"
