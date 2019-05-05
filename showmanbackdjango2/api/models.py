# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True, null=True)
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'




class FeeSchedule1(models.Model):
    id = models.IntegerField(primary_key=True)
    payment_date = models.DateField()
    payment_amount = models.IntegerField()

    class Meta:
        db_table = 'Fee_Schedule'


class EventTypes1(models.Model):
    id = models.IntegerField(primary_key=True)
    event_title = models.CharField(max_length=50, blank=True, null=True)
    event_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Event_Types'

class PaymentMethod1(models.Model):
    method_name = models.CharField(max_length=50)
    payment_id = models.ForeignKey(FeeSchedule1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Payment_Method'


class Country1(models.Model):
    id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Country'


class FederativeRepublic1(models.Model):
    id = models.IntegerField(primary_key=True)
    name_in_federation = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Federative_Republics'


class City1(models.Model):
    id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=50)
    city_state = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'City'


class Attendees1(models.Model):
    id = models.IntegerField(primary_key=True, )
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = 'Attendees'


class Address1(models.Model):
    id = models.IntegerField(primary_key=True)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    apartments = models.IntegerField()
    customer_id = models.ForeignKey(Attendees1, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Address'


class Discount1(models.Model):
    id = models.IntegerField(primary_key=True)
    orders_number = models.IntegerField()
    discount = models.IntegerField()
    customer_id = models.ForeignKey(Attendees1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Discount'


class OurEvents1(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.IntegerField()
    price = models.IntegerField()
    type_id = models.ForeignKey(EventTypes1, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(FeeSchedule1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Our_Events'


class ShowmanHouse1(models.Model):
    id = models.IntegerField(primary_key=True)
    employees_number = models.IntegerField()
    event_id = models.ForeignKey(EventTypes1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Showman_House'


class Orders1(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(EventTypes1, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Attendees1, on_delete=models.CASCADE)
    department_id = models.ForeignKey(ShowmanHouse1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Orders'


class Employees1(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    department_id = models.ForeignKey(ShowmanHouse1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Employees'


class AdministrativeStuff1(models.Model):
    id = models.IntegerField(primary_key=True)
    cab_number = models.IntegerField()
    employee_id = models.ForeignKey(Employees1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Administrative_stuff'


class EntertainingGroup1(models.Model):
    id = models.IntegerField(primary_key=True)
    house_per_week = models.IntegerField()
    employee_id = models.ForeignKey(Employees1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Entertaining_group'


class Trainee1(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    employee_id = models.ForeignKey(Employees1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Trainee'


class Avatars1(models.Model):
    id = models.IntegerField(primary_key=True)
    avatar = models.ImageField(upload_to='C:/xd_team.project/showmanhouseback/oracledbimages/',
                               default='C:/xd_team.project/showmanhouseback/oracledbimages/def/pepega.jpg')
    customer_id = models.ForeignKey(Attendees1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Avatars'