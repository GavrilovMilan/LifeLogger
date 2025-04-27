from django.db import models

# Create your models here.
class RefCurrency(models.Model):
    ref_currency_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    user_inserted = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user_updated = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False # Use existing table
        db_table = 'ref_currency'