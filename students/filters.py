import django_filters

from .models import CityModel,StateModel,CountryModel,StudentModel,EventModel,StudentParticipationModel

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = StudentModel
        fields = {
            'name':['icontains'],
            'student_id':['exact'],
            'id':['exact'],
            'branch':['icontains'],
            'batch_no':['icontains','exact'],
            'mob_no':['exact','icontains'],
            'email':['exact'],

        }

class CountryFilter(django_filters.FilterSet):
    class Meta:
        model = CountryModel
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains']
        }


class StateFilter(django_filters.FilterSet):
    class Meta:
        model = StateModel
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'country': ['exact'],
        }


class CityFilter(django_filters.FilterSet):
    class Meta:
        model = CityModel
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'state': ['exact'],
        }

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = EventModel
        fields ={
            'id':['exact'],
            'name':['exact','icontains'],
            'date_of_event':['gt','gte','lt','lte'],
            'no_of_days':['exact','gt','lt','lte','gte'],


        }

class StudentParticipationFilter(django_filters.FilterSet):
    class Meta:
        model = StudentParticipationModel
        fields = {
            'id':['exact'],
            'student':['exact'],
            'event':['exact'],
        }