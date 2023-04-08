# Generated by Django 4.0.8 on 2023-04-08 17:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boolean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean_code', models.CharField(default='0', max_length=1, unique=True, verbose_name='Boolean Code')),
                ('boolean_title', models.CharField(default='F', max_length=1, unique=True, verbose_name='Boolean Title')),
            ],
            options={
                'verbose_name_plural': 'Boolean',
                'db_table': 'boolean',
                'ordering': ['boolean_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MilepostTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milepost_template_code', models.CharField(max_length=10, unique=True, verbose_name='Milepost Template Code')),
                ('milepost_template_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Milepost Template Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Milepost Template',
                'db_table': 'milepost_template',
                'ordering': ['milepost_template_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UOMSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom_system_code', models.CharField(max_length=1, unique=True, verbose_name='UOM System Code')),
                ('uom_system_title', models.CharField(max_length=55, unique=True, verbose_name='UOM System Title')),
            ],
            options={
                'verbose_name_plural': 'Units of Measures System',
                'db_table': 'uom_system',
                'ordering': ['uom_system_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom_code', models.CharField(max_length=3, verbose_name='UOM Code')),
                ('uom_title', models.CharField(max_length=55, verbose_name='UOM Title')),
                ('uom_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g_measures.uomsystem', verbose_name='UOM System ID')),
            ],
            options={
                'verbose_name_plural': 'Units of Measures',
                'db_table': 'uom',
                'ordering': ['uom_code'],
                'managed': True,
                'unique_together': {('uom_system', 'uom_code')},
            },
        ),
        migrations.CreateModel(
            name='MilepostTemplateDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Step Number')),
                ('short_desc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Short Description')),
                ('long_desc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Long Description')),
                ('step_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Allocated Budget at this Step')),
                ('step_cum_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Cumulative Budget at this Step')),
                ('xref_tags_col_name_p', models.CharField(blank=True, default='mp_01_date_p', max_length=12, null=True, verbose_name='P Column Name X Ref')),
                ('xref_tags_col_name_e', models.CharField(blank=True, default='mp_01_date_e', max_length=12, null=True, verbose_name='E Column Name X Ref')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('milepost_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g_measures.mileposttemplate', verbose_name='Milepost Template ID')),
            ],
            options={
                'verbose_name_plural': 'Milepost Template Details',
                'db_table': 'milepost_template_detail',
                'ordering': [['milepost_template', 'step_no']],
                'managed': True,
                'unique_together': {('milepost_template', 'step_no')},
            },
        ),
    ]