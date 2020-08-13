from django.db import models
from ..base.models import TimeStampModel
from .constants import branches


class CountryModel(TimeStampModel):
    name = models.CharField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField(default=True)

class StateModel(TimeStampModel):
    name = models.CharField(max_length=1024,blank=True,null=True)
    country = models.ForeignKey(CountryModel,blank=True,null=True,related_name="state_country",on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)


class CityModel(TimeStampModel):
    name = models.CharField(max_length=1024,blank=True,null=True)
    state = models.ForeignKey(StateModel,blank=True,null=True,related_name="city_state",on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)



class StudentModel(TimeStampModel):
    name = models.CharField(max_length=1024,blank=True,null=True,)
    student_id = models.CharField(max_length=256, null=True, blank=True,unique=True)
    branch = models.CharField(max_length=1024,blank=True,null=True)
    batch_no = models.IntegerField(blank=True,null=True)
    reg_no = models.IntegerField(max_length=14,blank=True,null=True,unique=True)
    address = models.CharField(max_length=1024,blank=True,null=True)
    locality = models.CharField(max_length=1024,blank=True,null=True)
    city = models.ForeignKey(CityModel,blank=True,null=True,on_delete=models.PROTECT)
    state = models.ForeignKey(StateModel,blank=True,null=True,on_delete=models.PROTECT)
    country = models.ForeignKey(CountryModel,blank=True,null=True,on_delete=models.PROTECT)
    pincode = models.IntegerField(blank=True,null=True)
    mob_no = models.IntegerField(max_length=15,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    is_active = models.BooleanField(default=True)



class EventModel(TimeStampModel):
    name = models.CharField(max_length=256,blank=True,null=True,)
    min_requirements = models.TextField(blank=True,null=True)
    date_of_event = models.DateField(blank=True,null=True)
    no_of_days = models.IntegerField(blank=True,null=True)
    rel_branch = models.CharField(choices=branches,blank=True,null=True)
    is_active = models.BooleanField(default=True)

class StudentParticipationModel(TimeStampModel):
    student = models.ForeignKey(StudentModel,blank=True,null=True,related_name="participation_student")
    event = models.ForeignKey(EventModel,blank=True,null=True,related_name="participation_event")
    is_active = models.BooleanField(default=True)











