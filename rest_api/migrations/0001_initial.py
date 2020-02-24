# Generated by Django 3.0.3 on 2020-02-24 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_type', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
                ('price', models.CharField(max_length=25)),
                ('rent_price', models.PositiveIntegerField(blank=True, null=True)),
                ('bedrooms', models.PositiveSmallIntegerField()),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('area_unit', models.CharField(default='SqFt', max_length=20)),
                ('home_size', models.PositiveIntegerField(blank=True, null=True)),
                ('property_size', models.PositiveIntegerField(blank=True, null=True)),
                ('year_built', models.PositiveIntegerField(blank=True, null=True)),
                ('zillow_id', models.IntegerField(unique=True)),
                ('link', models.TextField(unique=True)),
                ('zestimate_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('zestimate_last_updated', models.DateField(default=datetime.date(1970, 1, 1))),
                ('rentzestimate_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('rentzestimate_last_updated', models.DateField(default=datetime.date(1970, 1, 1))),
                ('tax_year', models.PositiveIntegerField()),
                ('tax_value', models.PositiveIntegerField()),
                ('last_sold_date', models.DateField(blank=True, null=True)),
                ('last_sold_price', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('address', 'zipcode')},
            },
        ),
    ]
