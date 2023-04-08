# Generated by Django 4.0.8 on 2023-04-08 17:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a_hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryTransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_transaction_type_code', models.CharField(max_length=1, unique=True, verbose_name='Inventory Transaction Type Code')),
                ('inventory_transaction_type_title', models.CharField(max_length=55, unique=True, verbose_name='Inventory Transaction Type Title')),
            ],
            options={
                'verbose_name_plural': 'Inventory Transaction Types',
                'db_table': 'inventory_transaction_type',
                'ordering': ['inventory_transaction_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaterialStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_status_code', models.CharField(max_length=2, unique=True, verbose_name='Material Status Code')),
                ('material_status_title', models.CharField(max_length=55, unique=True, verbose_name='Material Status Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Material Statuses',
                'db_table': 'material_status',
                'ordering': ['material_status_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderDetailStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_detail_status_code', models.CharField(max_length=1, unique=True, verbose_name='Order Detail Status Code')),
                ('order_detail_status_title', models.CharField(max_length=55, unique=True, verbose_name='Order Detail Status Title')),
            ],
            options={
                'verbose_name_plural': 'Order Details Status',
                'db_table': 'order_detail_status',
                'ordering': ['order_detail_status_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status_code', models.CharField(max_length=1, unique=True, verbose_name='Orders Status Code')),
                ('order_status_title', models.CharField(max_length=55, unique=True, verbose_name='Orders Status Title')),
            ],
            options={
                'verbose_name_plural': 'Orders Status',
                'db_table': 'order_status',
                'ordering': ['order_status_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrderTaxStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_tax_status_code', models.CharField(max_length=1, unique=True, verbose_name='Order Tax Status Code')),
                ('order_tax_status_title', models.CharField(max_length=55, unique=True, verbose_name='Order Tax Status Title')),
            ],
            options={
                'verbose_name_plural': 'Orders Tax Status',
                'db_table': 'order_tax_status',
                'ordering': ['order_tax_status_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PayMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method_code', models.CharField(max_length=1, unique=True, verbose_name='Pay Method Code')),
                ('pay_method_title', models.CharField(max_length=55, unique=True, verbose_name='Pay Method Title')),
            ],
            options={
                'verbose_name_plural': 'Payment Methods',
                'db_table': 'pay_method',
                'ordering': ['pay_method_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order_status_code', models.CharField(max_length=1, unique=True, verbose_name='PO Status Code')),
                ('purchase_order_status_title', models.CharField(max_length=55, unique=True, verbose_name='PO Status Title')),
            ],
            options={
                'verbose_name_plural': 'Purchase Order Statuses',
                'db_table': 'purchase_order_status',
                'ordering': ['purchase_order_status_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_commit_code', models.CharField(max_length=55, unique=True, verbose_name='PO/Commit Package Code')),
                ('po_commit_title', models.CharField(max_length=200, unique=True, verbose_name='PO/Commit Package Title')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='PO Creation Date')),
                ('submit_date', models.DateTimeField(blank=True, null=True, verbose_name='PO Submission Date')),
                ('expect_date', models.DateTimeField(blank=True, null=True, verbose_name='Order Expected Date')),
                ('shipping_fee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, verbose_name='Shipping Fee')),
                ('taxes', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, verbose_name='Taxes')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='Payment Date')),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999999)], verbose_name='Payment Amount')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('approve_date', models.DateTimeField(blank=True, null=True, verbose_name='Approval Date')),
                ('approve_by_personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approve_by_personnel', to='a_hr.personnel', verbose_name='Approved By')),
                ('create_by_personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_by_personnel', to='a_hr.personnel', verbose_name='Created By')),
                ('pay_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='d_mm.paymethod', verbose_name='Pay Method ID')),
                ('purchase_order_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='d_mm.purchaseorderstatus', verbose_name='Purchase Order Status ID')),
                ('submit_by_personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submit_by_personnel', to='a_hr.personnel', verbose_name='Submitted By')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_hr.company', verbose_name='Supplier ID')),
            ],
            options={
                'verbose_name_plural': 'Purchase Orders - Commit Packages',
                'db_table': 'purchase_order',
                'ordering': ['po_commit_code'],
                'managed': True,
            },
        ),
    ]