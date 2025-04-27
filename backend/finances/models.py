# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FinExpenses(models.Model):
    fin_expenses_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    amount = models.FloatField()
    description = models.CharField(max_length=128, blank=True, null=True)
    ref_category = models.ForeignKey('RefCategory', models.DO_NOTHING)
    ref_means_of_payment = models.ForeignKey('RefMeansOfPayment', models.DO_NOTHING)
    user_inserted = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    user_updated = models.CharField(max_length=100)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fin_expenses'


class FinIncome(models.Model):
    fin_income_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    amount = models.FloatField()
    description = models.CharField(max_length=128, blank=True, null=True)
    ref_category = models.ForeignKey('RefCategory', models.DO_NOTHING)
    ref_means_of_payment = models.ForeignKey('RefMeansOfPayment', models.DO_NOTHING)
    user_inserted = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    user_updated = models.CharField(max_length=100)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fin_income'


class RefCategory(models.Model):
    ref_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rashod = models.IntegerField(db_comment='0 - NE; -1 - DA')
    prihod = models.IntegerField(db_comment='0 - NE; -1 - DA')
    user_inserted = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    user_updated = models.CharField(max_length=100)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ref_category'


class RefCurrency(models.Model):
    ref_currency_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    user_inserted = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    user_updated = models.CharField(max_length=100)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ref_currency'


class RefMeansOfPayment(models.Model):
    ref_means_of_payment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256, blank=True, null=True)
    user_inserted = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    user_updated = models.CharField(max_length=100)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ref_means_of_payment'
