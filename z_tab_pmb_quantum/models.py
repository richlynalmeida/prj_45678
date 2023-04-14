from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from a_hr.models import Personnel, RaciMatrixDefinition, StakeholderRoles
from b_wbs.models import CostTypeClass, CostType, Department, Discipline, WBSType, WBS, FacilitySystem, \
    FacilitySystemDetail, PmbL03WpExecutionType, PmbL04WpExecutionType, PmbL03WpStatusType, PmbL04WpStatusType
# from b_benchmarking.models import ProjectPhases, ProjectStages
from e_commodities.models import CommodityType, Commodity
# from f_contracts.models import Contract, TrendTypes
from g_measures.models import UOM
from h_schedules.models import PMBL03Schedule, PMBL04Schedule
from d_mm.models import PurchaseOrder
from django.db import models
from d_mm.models import MaterialStatus
from e_commodities.models import CommodityDetail
from g_measures.models import MilepostTemplate


class ProjectPhases(models.Model):
    project_phase_code = models.CharField(unique=True, max_length=5, verbose_name='Project Phase Code')
    project_phase_title = models.CharField(max_length=55, blank=True, null=True, verbose_name='Project Phase Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = 'Project Phases'
        db_table = 'project_phase'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_phase_code']

    def __str__(self):
        return str('%s' % self.project_phase_code)


class ProjectStages(models.Model):
    project_stage_code = models.CharField(unique=True, max_length=5, verbose_name='Project Stage Code')
    project_stage_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                                   verbose_name='Project Status Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Project Stages"
        db_table = 'project_stage'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_stage_code']

    def __str__(self):
        return f"{self.project_stage_code} - {self.project_stage_title}"


class PmbL03Wp(models.Model):
    pmb_L03_wp_exe_type = models.ForeignKey(PmbL03WpExecutionType, on_delete=models.CASCADE,
                                            verbose_name='PMB L03 WP Execution Type ID', default=1)
    pmb_L03_wp_status_type = models.ForeignKey(PmbL03WpStatusType, on_delete=models.CASCADE,
                                               verbose_name='PMB L03 WP Status Type ID', default=1)
    wbs = models.ForeignKey(WBS, on_delete=models.CASCADE,
                            verbose_name='WBS ID', default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   verbose_name='CBWP Department ID', default=1)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   verbose_name='CBWP Discipline ID', default=1)
    pmb_L03_schedule = models.ForeignKey(PMBL03Schedule, on_delete=models.CASCADE,
                                         verbose_name='PMB L03 Schedule Activity ID', default=1)
    disc_start_date = models.DateTimeField(blank=True, null=True,
                                           verbose_name='Discretionary Start Date')
    disc_finish_date = models.DateTimeField(blank=True, null=True,
                                            verbose_name='Discretionary Finish Date')
    facility_system_detail = models.ForeignKey(FacilitySystemDetail, on_delete=models.CASCADE,
                                               verbose_name='CBWP Facility System Detail ID', default=1)
    pmb_wp_parent = models.ForeignKey('z_tab_pmb_quantum.PmbL03Wp', on_delete=models.CASCADE,
                                      verbose_name='Parent ID', null=True, blank=True, default=1)
    primary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                       verbose_name='CBWP Primary Contact or Owner')
    secondary_contact = models.CharField(unique=False, max_length=100, blank=True, null=True,
                                         verbose_name='CBWP Secondary Contact')
    pmb_L03_wp_code = models.CharField(unique=True, max_length=55, verbose_name='PMB L03 WP Code')
    pmb_L03_wp_title = models.CharField(unique=False, max_length=200, blank=True, null=True,
                                        verbose_name='PMB L03 WP Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')
    ocb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OCB Hours', default=0)
    ocb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OCB Costs', default=0)
    # Trend Control Budget
    # tcb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='TCB Quantity', default=0)
    # tcb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='TCB UOM ID', default=1,
    #                             related_name='tcb_uom')
    tcb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TCB Hours', default=0)
    tcb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TCB Costs', default=0)
    # Current Control Budget
    # ccb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='CCB Quantity', default=0)
    # ccb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CCB UOM ID', default=1,
    #                             related_name='ccb_uom')
    ccb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CCB Hours', default=0)
    ccb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CCB Costs', default=0)
    # Trend Forecast Budget
    # tfb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='TFB Quantity', default=0)
    # tfb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='TFB UOM ID', default=1,
    #                             related_name='tfb_uom')
    tfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TFB Hours', default=0)
    tfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TFB Costs', default=0)
    # Current Forecast Budget
    # cfb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='CFB Quantity', default=0)
    # cfb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CFB UOM ID', default=1,
    #                             related_name='cfb_uom')
    cfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CFB Hours', default=0)
    cfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CFB Costs', default=0)

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 Work Packages"
        db_table = 'pmb_L03_wp'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['pmb_L03_wp_code']

    def __str__(self):
        return f"{self.pmb_L03_wp_code} - {self.pmb_L03_wp_title}"


class PmbL03WpCa(models.Model):
    pmb_L03_wp = models.ForeignKey(PmbL03Wp, on_delete=models.CASCADE,
                                   verbose_name='PMB L03 WP ID', default=1)
    stakeholder_role = models.ForeignKey(StakeholderRoles, on_delete=models.CASCADE, verbose_name='Stakeholder Role ID',
                                         default=1)
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE, verbose_name='CBWP Cost Type ID',
                                  default=1)
    pmb_L03_wp_ca_code = models.CharField(unique=True, max_length=55, verbose_name='PMB L03 WP CA Code')
    pmb_L03_wp_ca_title = models.CharField(unique=False, max_length=200, blank=True, null=True,
                                           verbose_name='PMB L03 WP CA Title')
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    # ocb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='OCB Quantity', default=0)
    # ocb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='OCB UOM ID', default=1,
    #                             related_name='ocb_uom')
    ocb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OCB Hours', default=0)
    ocb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='OCB Costs', default=0)
    # Trend Control Budget
    # tcb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='TCB Quantity', default=0)
    # tcb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='TCB UOM ID', default=1,
    #                             related_name='tcb_uom')
    tcb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TCB Hours', default=0)
    tcb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TCB Costs', default=0)
    # Current Control Budget
    # ccb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='CCB Quantity', default=0)
    # ccb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CCB UOM ID', default=1,
    #                             related_name='ccb_uom')
    ccb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CCB Hours', default=0)
    ccb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CCB Costs', default=0)
    # Trend Forecast Budget
    # tfb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='TFB Quantity', default=0)
    # tfb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='TFB UOM ID', default=1,
    #                             related_name='tfb_uom')
    tfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TFB Hours', default=0)
    tfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='TFB Costs', default=0)
    # Current Forecast Budget
    # cfb_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                    verbose_name='CFB Quantity', default=0)
    # cfb_uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CFB UOM ID', default=1,
    #                             related_name='cfb_uom')
    cfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CFB Hours', default=0)
    cfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='CFB Costs', default=0)

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 WP Cost Accounts"
        db_table = 'pmb_L03_wp_ca'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['pmb_L03_wp_ca_code']

    def __str__(self):
        return f"{self.pmb_L03_wp_ca_code} - {self.pmb_L03_wp_ca_title}"


class TrendTypes(models.Model):
    trend_type_code = models.CharField(unique=True, max_length=5,
                                       verbose_name='Trend Type Code')
    trend_type_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                        verbose_name='Trend Type Title')
    scope_related_check = models.IntegerField(default=0, verbose_name='Scope Related Check')

    # 0 - Non-Scope Related; 1 - Scope Related

    class Meta:
        managed = True
        verbose_name_plural = "Trend Types"
        db_table = 'tm_trend_type'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['trend_type_code']

    # def __str__(self):
    #     return str('%s' % self.contract_pricing_style_code)
    def __str__(self):
        return f"{self.trend_type_code} - {self.trend_type_title}"


class TrendApprovalStatuses(models.Model):
    trend_approval_status_code = models.CharField(unique=True, max_length=5,
                                                  verbose_name='Trend Approval Status Code')
    trend_approval_status_title = models.CharField(unique=True, max_length=55, blank=True, null=True,
                                                   verbose_name='Trend Approval Status Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        verbose_name_plural = "Trend Approval Statuses"
        db_table = 'tm_trend_approval_status'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['trend_approval_status_code']

    # def __str__(self):
    #     return str('%s' % self.contract_pricing_style_code)
    def __str__(self):
        return f"{self.trend_approval_status_code} - {self.trend_approval_status_title}"


class Trends(models.Model):
    # from_pmb_L03_wp_ca = models.ForeignKey(PmbL03WpCa, on_delete=models.CASCADE, null=True,
    #                                        verbose_name='From PMB L03 WP CA ID', default=1,
    #                                        related_name='from_pmb_L03_wp_ca')
    # to_pmb_L03_wp_ca = models.ForeignKey(PmbL03WpCa, on_delete=models.CASCADE, null=True,
    #                                        verbose_name='To PMB L03 WP CA ID', default=1,
    #                                      related_name='to_pmb_L03_wp_ca')
    tm_trend_type = models.ForeignKey(TrendTypes, on_delete=models.CASCADE,
                                      verbose_name='Trend Type ID', default=1)
    tm_trend_approval_status = models.ForeignKey(TrendApprovalStatuses, on_delete=models.CASCADE,
                                                 verbose_name='Trend Approval Status ID', default=1)
    # project_phase = models.ForeignKey(ProjectPhases, on_delete=models.CASCADE,
    #                                   verbose_name='Project Phase ID', default=1)
    # project_stage = models.ForeignKey(ProjectStages, on_delete=models.CASCADE,
    #                                   verbose_name='Project Stage ID', default=1)
    # trend_code = models.CharField(unique=True, max_length=5,
    #                               verbose_name='Trend Approval Status Code')
    trend_title = models.CharField(unique=False, max_length=55, blank=False, null=False,
                                   verbose_name='Trend Title')
    trend_desc = models.CharField(max_length=2000, verbose_name='Trend Description', blank=True, null=True,)
    trend_hours = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Trend Hours', default=0,
                                      blank=True, null=True,)
    trend_costs = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Trend Costs', default=0,
                                      blank=False, null=False,)
    modified_date = models.DateTimeField(verbose_name='Modified Date',blank=True, null=True,)

    class Meta:
        managed = True
        verbose_name_plural = "Trends"
        db_table = 'tm_trend'
        app_label = 'z_tab_pmb_quantum'
        # ordering = ['trend_code']
        unique_together = ['tm_trend_type', 'tm_trend_approval_status', 'trend_title']

    # def __str__(self):
    #     return str('%s' % self.contract_pricing_style_code)
    def __str__(self):
        return f"{self.trend_title}"


class PmbL03WpCaDetails(models.Model):
    pmb_L03_wp_ca = models.ForeignKey(PmbL03WpCa, on_delete=models.CASCADE,
                                      verbose_name='PMB L03 WP CA ID', default=1)
    tm_trend = models.ForeignKey(Trends, on_delete=models.CASCADE,
                                 verbose_name='Trend ID', default=1)
    transaction_type = models.CharField(unique=False, max_length=10, verbose_name='Transaction Type')
    # Quantification, Pricing, Hours and Costs
    quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                   verbose_name='Quantity', default=0)
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='UOM ID', default=1)
    hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                verbose_name='Hours', default=0)
    costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                verbose_name='Costs', default=0)
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    modified_date = models.DateTimeField(unique=False, verbose_name='Modified Date')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 WP Cost Account Details"
        db_table = 'pmb_L03_wp_ca_detail'
        app_label = 'z_tab_pmb_quantum'
        # ordering = ['pmb_L03_wp_ca_scope_item_code']
        # unique_together = [
        #     ['pmb_L03_wp_ca_scope_item_code', 'pmb_L03_wp_ca_scope_item_title', 'pmb_L03_wp_ca_scope_item_no']]

    def __str__(self):
        return f"{self.pmb_L03_wp_ca} - {self.tm_trend} " \
               f"- {self.modified_date}"


class PmbL03WpCaScopeItems(models.Model):
    pmb_L03_wp_ca = models.ForeignKey(PmbL03WpCa, on_delete=models.CASCADE,
                                      verbose_name='PMB L03 WP CA ID', default=1)
    pmb_L03_wp_ca_scope_item_code = models.CharField(unique=True, max_length=55, verbose_name='PMB L03 WP CA Scope '
                                                                                              'Item Code')
    pmb_L03_wp_ca_scope_item_title = models.CharField(unique=False, max_length=200, blank=True, null=True,
                                                      verbose_name='PMB L03 WP CA Scope Item Title')
    pmb_L03_wp_ca_scope_item_no = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],
                                                      verbose_name='Step Number')
    # scope_item_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                           verbose_name='Scope Item Quantity', default=0)
    # uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    scope_item_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                           verbose_name='Scope Item Hours', default=0)
    scope_item_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                           verbose_name='Scope Item Costs', default=0)
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 WP Cost Account Scope or Contract Pay Items"
        db_table = 'pmb_L03_wp_ca_scope_item'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['pmb_L03_wp_ca_scope_item_code']
        unique_together = [
            ['pmb_L03_wp_ca_scope_item_code', 'pmb_L03_wp_ca_scope_item_title', 'pmb_L03_wp_ca_scope_item_no']]

    def __str__(self):
        return f"{self.pmb_L03_wp_ca_scope_item_code} - {self.pmb_L03_wp_ca_scope_item_title} " \
               f"- {self.pmb_L03_wp_ca_scope_item_no}"


class PmbL03WpCaScopeItemDetails(models.Model):
    pmb_L03_wp_ca_scope_item = models.ForeignKey(PmbL03WpCaScopeItems, on_delete=models.CASCADE,
                                                 verbose_name='PMB L03 WP CA Scope Item ID', default=1)
    transaction_type = models.CharField(unique=False, max_length=10, verbose_name='Transaction Type')
    # Quantification, Pricing, Hours and Costs
    # Original Control Budget aka Final Estimate Budget
    quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                   verbose_name='Quantity', default=0)
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                verbose_name='Hours', default=0)
    costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                verbose_name='Costs', default=0)
    comments = models.CharField(blank=False, null=False, max_length=2000, verbose_name='Comments')
    modified_date = models.DateTimeField(verbose_name='Modified Date')

    class Meta:
        managed = True
        verbose_name_plural = "PMB L03 WP Cost Account Scope or Contract Pay Item Details"
        db_table = 'pmb_L03_wp_ca_scope_item_detail'
        app_label = 'z_tab_pmb_quantum'
        # ordering = ['pmb_L03_wp_ca_scope_item_code']
        # unique_together = [
        #     ['pmb_L03_wp_ca_scope_item_code', 'pmb_L03_wp_ca_scope_item_title', 'pmb_L03_wp_ca_scope_item_no']]

    def __str__(self):
        return f"{self.pmb_L03_wp_ca_scope_item} - {self.modified_date}"


class PmbL04Wp(models.Model):
    pmb_L03_wp_ca = models.ForeignKey(PmbL03WpCa, on_delete=models.CASCADE,
                                      verbose_name='PMB L03 WP CA ID ID', default=1)
    pmb_L04_wp_exe_type = models.ForeignKey(PmbL04WpExecutionType, on_delete=models.CASCADE,
                                            verbose_name='PMB L04 WP Execution Type ID', default=1)
    pmb_L04_wp_status_type = models.ForeignKey(PmbL04WpStatusType, on_delete=models.CASCADE,
                                               verbose_name='PMB L04 WP Status Type ID', default=1)
    commodity_type = models.ForeignKey(CommodityType, on_delete=models.CASCADE,
                                       verbose_name='CBWP Commodity Type ID', default=1)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='CBWP Commodity ID', default=1)
    pmb_L04_schedule = models.ForeignKey(PMBL04Schedule, on_delete=models.CASCADE,
                                         verbose_name='PMB L04 Schedule Activity ID', default=1)
    disc_start_date = models.DateTimeField(blank=True, null=True,
                                           verbose_name='Discretionary Start Date')
    disc_finish_date = models.DateTimeField(blank=True, null=True,
                                            verbose_name='Discretionary Finish Date')
    pmb_L04_wp_code = models.CharField(unique=True, max_length=55, verbose_name='PMB L04 WP Code')
    pmb_L04_wp_title = models.CharField(unique=False, max_length=200, blank=True, null=True,
                                        verbose_name="PMB L04 WP Title")
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    # Quantification, Pricing, Hours and Costs
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    # Current Forecast Budget
    bac_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                       verbose_name='BAC Quantity', default=0)
    bac_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='BAC Hours', default=0)
    bac_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                    verbose_name='BAC Costs', default=0)

    class Meta:
        managed = True
        verbose_name_plural = "PMB L04 Work Packages"
        db_table = 'pmb_L04_wp'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['pmb_L04_wp_code']

    def __str__(self):
        return f"{self.pmb_L04_wp_code} - {self.pmb_L04_wp_title}"


class ProjectComponent(models.Model):
    # A project component technically is a unique thing on a project, however we need the ability to reuse it
    # with the same identification across multiple functions. For e.g A pump "ABC-001" needs to be identified
    # and tracked during installation, but it 'may' need to be identified and tracked again during startup. These are
    # two separate activities with individual costs. For now, let us group the 'id' along with the 'function' for
    # uniqueness on the project.
    project_component_code = models.CharField(unique=True, max_length=25, verbose_name='Project Component Code')
    project_component_title = models.CharField(unique=False, max_length=55, blank=True, null=True,
                                               verbose_name='Project Component Title')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Component Comments')

    # qty to be added here as this would represent client base quantities.

    class Meta:
        managed = True
        verbose_name_plural = "Project Components"
        db_table = 'project_component'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_component_code']

    def __str__(self):
        return str('%s' % self.project_component_code)


class ProjectDocument(models.Model):
    project_document_code = models.CharField(unique=True, max_length=25, verbose_name='Project Document Code')
    project_document_title = models.CharField(unique=False, max_length=100, verbose_name='Project Document Title')
    revision_number = models.CharField(max_length=3, blank=True, null=True, verbose_name='Revision No')
    revision_status = models.CharField(max_length=55, blank=True, null=True, verbose_name='Revision Status')
    release_date = models.DateTimeField(blank=True, null=True, verbose_name='Release Date')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Project Document Comments')
    document_attachment = models.FileField(blank=True, null=True, upload_to='Documents/',
                                           verbose_name='Document Attachment')
    document_url = models.URLField(blank=True, null=True, max_length=250,
                                   verbose_name='Document URL')

    class Meta:
        managed = True
        verbose_name_plural = "Project Documents"
        db_table = 'project_document'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_document_code']

    def __str__(self):
        return str('%s' % self.project_document_code)


class ProjectDocumentComponent(models.Model):
    # This is a junction table which joins a component with a document. It is the best form of uniqueness, but can be
    # overkill on some projects. The idea is to use (link) this unified widget in the csl_d_deliverables app for
    # tracking. The premise being that a unified_widget may still be on a very high level for tracking and may
    # need to be broken down some more for takeoff and tracking.
    project_document_component_code = models.CharField(unique=True, max_length=25,
                                                       verbose_name='Project Unified Document Component Code',
                                                       default='Test')
    project_document_component_title = models.CharField(unique=False, blank=True, null=True, max_length=100,
                                                        verbose_name='Project Unified Document Component Code Title')
    project_component = models.ForeignKey(ProjectComponent,
                                          on_delete=models.CASCADE, verbose_name='Project Component ID', default=1)
    project_document = models.ForeignKey(ProjectDocument,
                                         on_delete=models.CASCADE, verbose_name='Project Document ID', default=1)

    class Meta:
        managed = True
        verbose_name_plural = "Project Unified Documents Components"
        db_table = 'project_document_component'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['project_document_component_code']

    def __str__(self):
        return str('%s' % self.project_document_component_code)


class PmbL04WpQuantum(models.Model):
    pmb_L04_wp = models.ForeignKey(PmbL04Wp, on_delete=models.CASCADE,
                                   verbose_name='PMB L04 WP ID', default=1)
    quantum_code = models.CharField(unique=True, max_length=55, verbose_name='Quantum Code')
    quantum_title = models.CharField(unique=False, max_length=200, blank=True, null=True,
                                     verbose_name='Quantum Title')
    comments = models.CharField(max_length=200, blank=True, null=True, verbose_name='CBWP Comments')
    # Quantification, Pricing, Hours and Costs
    # uom = models.ForeignKey(UOM, on_delete=models.CASCADE, verbose_name='CBWP UOM ID', default=1)
    # Current Forecast Budget
    bac_quantum_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
                                               verbose_name='BAC Quantum Quantity', default=0)
    # cfb_hours = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                 verbose_name='CFB Hours', default=0)
    # cfb_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                 verbose_name='CFB Costs', default=0)
    project_document_component = models.ForeignKey(ProjectDocumentComponent, blank=True, null=True,
                                                   on_delete=models.CASCADE,
                                                   verbose_name='Project Document Component ID',
                                                   default=1)
    material_status = models.ForeignKey(MaterialStatus, on_delete=models.CASCADE,
                                        verbose_name='Material Status ID', default=1)
    commodity_detail = models.ForeignKey(CommodityDetail, on_delete=models.CASCADE,
                                         verbose_name='Commodity Detail ID', default=1)
    milepost_template = models.ForeignKey(MilepostTemplate, on_delete=models.CASCADE,
                                          verbose_name='Milepost Template ID', default=1)
    # cad_id = models.CharField(max_length=55, blank=True, null=True, verbose_name='CAD ID')
    mp_01_date_p = models.DateTimeField(verbose_name='1st Planned MP Date', blank=True, null=True, )
    mp_01_date_e = models.DateTimeField(verbose_name='1st Earned MP Date', blank=True, null=True, )
    mp_02_date_p = models.DateTimeField(verbose_name='2nd Planned MP Date', blank=True, null=True, )
    mp_02_date_e = models.DateTimeField(verbose_name='2nd Earned MP Date', blank=True, null=True, )
    mp_03_date_p = models.DateTimeField(verbose_name='3rd Planned MP Date', blank=True, null=True, )
    mp_03_date_e = models.DateTimeField(verbose_name='3rd Earned MP Date', blank=True, null=True, )
    mp_04_date_p = models.DateTimeField(verbose_name='4th Planned MP Date', blank=True, null=True, )
    mp_04_date_e = models.DateTimeField(verbose_name='4th Earned MP Date', blank=True, null=True, )
    mp_05_date_p = models.DateTimeField(verbose_name='05th Planned Milepost Date', blank=True, null=True, )
    mp_05_date_e = models.DateTimeField(verbose_name='05th Earned Milepost Date', blank=True, null=True, )
    mp_06_date_p = models.DateTimeField(verbose_name='06th Planned Milepost Date', blank=True, null=True, )
    mp_06_date_e = models.DateTimeField(verbose_name='06th Earned Milepost Date', blank=True, null=True, )
    mp_07_date_p = models.DateTimeField(verbose_name='07th Planned Milepost Date', blank=True, null=True, )
    mp_07_date_e = models.DateTimeField(verbose_name='07th Earned Milepost Date', blank=True, null=True, )
    mp_08_date_p = models.DateTimeField(verbose_name='08th Planned Milepost Date', blank=True, null=True, )
    mp_08_date_e = models.DateTimeField(verbose_name='08th Earned Milepost Date', blank=True, null=True, )
    mp_09_date_p = models.DateTimeField(verbose_name='09th Planned Milepost Date', blank=True, null=True, )
    mp_09_date_e = models.DateTimeField(verbose_name='09th Earned Milepost Date', blank=True, null=True, )
    mp_10_date_p = models.DateTimeField(verbose_name='10th Planned Milepost Date', blank=True, null=True, )
    mp_10_date_e = models.DateTimeField(verbose_name='10th Earned Milepost Date', blank=True, null=True, )

    class Meta:
        managed = True
        verbose_name_plural = "PMB L04 WP Quantum Details"
        db_table = 'pmb_L04_wp_quantum'
        app_label = 'z_tab_pmb_quantum'
        ordering = ['quantum_code']

    def __str__(self):
        return f"{self.quantum_code} - {self.quantum_title}"
