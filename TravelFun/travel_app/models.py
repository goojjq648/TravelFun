# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Counties(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'counties'


class Taiwen(models.Model):
    taiwen_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=20)
    town = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'taiwen'


class Travel(models.Model):
    travel_id = models.AutoField(primary_key=True)
    travel_name = models.CharField(max_length=50)
    travel_txt = models.TextField(blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    travel_address = models.TextField()
    region = models.CharField(max_length=10)
    town = models.CharField(max_length=10)
    travel_linginfo = models.TextField(blank=True, null=True)
    opentime = models.TextField(blank=True, null=True)
    image1 = models.TextField(blank=True, null=True)
    image2 = models.TextField(blank=True, null=True)
    image3 = models.TextField(blank=True, null=True)
    px = models.DecimalField(db_column='Px', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    py = models.DecimalField(db_column='Py', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    class1 = models.ForeignKey('TravelClass', models.DO_NOTHING, db_column='class1')
    class2 = models.ForeignKey('TravelClass', models.DO_NOTHING, db_column='class2', related_name='travel_class2_set', blank=True, null=True)
    class3 = models.ForeignKey('TravelClass', models.DO_NOTHING, db_column='class3', related_name='travel_class3_set', blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    ticketinfo = models.TextField(blank=True, null=True)
    parkinginfo = models.TextField(blank=True, null=True)
    upload = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel'


class TravelClass(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'travel_class'
