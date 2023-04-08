from django.db import models
from djmoney.models.fields import MoneyField
from z_tab_pmb_quantum.models import PmbL04Wp


class FinanceTransactionType(models.Model):
    finance_transaction_type_code = models.CharField(unique=True, max_length=1,
                                                       verbose_name='Finance Transaction Type Code')
    finance_transaction_type_title = models.CharField(unique=True, max_length=55,
                                                        verbose_name='Finance Transaction Type Title')

    class Meta:
        managed = True
        verbose_name_plural = "Finance Transaction Types"
        db_table = 'finance_transaction_type'
        app_label = 'f_finance'
        ordering = ['finance_transaction_type_code']

    def __str__(self):
        return f"{self.finance_transaction_type_code} - {self.finance_transaction_type_title}"


class PmbL04WpAccountsReceivable(models.Model):
    pmb_L04_wp = models.ForeignKey(PmbL04Wp, on_delete=models.CASCADE, verbose_name='PMB L04 WP ID')
    calendar_date = models.DateTimeField(verbose_name='Calendar Date')
    # ar_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                verbose_name='Accounts Receivable Costs on Calendar Date', default=0)
    ar_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                          verbose_name='Accounts Receivable Costs on Calendar Date',
                          default_currency='CAD')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        unique_together = (('pmb_L04_wp', 'calendar_date'),)
        verbose_name_plural = "PMB L04 WP Accounts Receivable"
        db_table = 'pmb_L04_wp_ar'
        app_label = 'f_finance'
        ordering = ['pmb_L04_wp', 'calendar_date']

    def __bytes__(self):
        return bytes('%s %s' % (self.calendar_date, self.pmb_L04_wp))


class PmbL04WpAccountsPayable(models.Model):
    pmb_L04_wp = models.ForeignKey(PmbL04Wp, on_delete=models.CASCADE, verbose_name='PMB L04 WP ID')
    calendar_date = models.DateTimeField(verbose_name='Calendar Date')
    # ar_costs = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True,
    #                                verbose_name='Accounts Receivable Costs on Calendar Date', default=0)
    ap_costs = MoneyField(max_digits=18, decimal_places=2, blank=True, null=True,
                          verbose_name='Accounts Payable Costs on Calendar Date',
                          default_currency='CAD')
    comments = models.CharField(max_length=2000, blank=True, null=True, verbose_name='Comments')

    class Meta:
        managed = True
        unique_together = (('pmb_L04_wp', 'calendar_date'),)
        verbose_name_plural = "PMB L04 WP Accounts Payable"
        db_table = 'pmb_L04_wp_ap'
        app_label = 'f_finance'
        ordering = ['pmb_L04_wp', 'calendar_date']

    def __bytes__(self):
        return bytes('%s %s' % (self.calendar_date, self.pmb_L04_wp))