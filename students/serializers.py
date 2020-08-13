from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from .models import CityModel,StateModel,CountryModel,StudentModel,EventModel,StudentParticipationModel

class CountrySerializer(ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'

class StateSerializer(ModelSerializer):
    class Meta:
        model = StateModel
        fields = '__all__'

class CitySerializer(ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    city_extra = serializers.CharField(max_length=1024,required=False)
    state_extra = serializers.CharField(max_length=1024,required=False)
    country_extra = serializers.CharField(max_length=1024,required=False)
    city_data = serializers.SerializerMethodField(required=False)
    state_data = serializers.SerializerMethodField(required=False)
    country_data = serializers.SerializerMethodField(required=False)

    class Meta:
        model = StudentModel
        fields = '__all__'

    def create(self,validated_data):
        city_extra = validated_data.pop('city_extra',None)
        state_extra = validated_data.pop('state_extra',None)
        country_extra = validated_data.pop('country_extra',None)
        student_id = validated_data.get('student_id',None)
        batch_no = validated_data.get('batch_no',None)
        branch = validated_data.get('branch',None)

        if city_extra:
            validated_data['city'] = CityModel.objects.create(name = city_extra)
        if state_extra:
            validated_data['state'] = StateModel.objects.create(name = state_extra)
        if country_extra:
            validated_data['country'] = CountryModel.objects.create(name = country_extra)

        instance = StudentModel.objects.create(**validated_data)
        if not student_id:
            instance.student_id = str(batch_no) + str(branch) + str(instance.pk)
        instance.save()
        return instance

    def update(self,instance,validated_data):
        city_extra = validated_data.pop('city_extra', None)
        state_extra = validated_data.pop('state_extra', None)
        country_extra = validated_data.pop('country_extra', None)
        mob_no = validated_data.get('mob_no',None)
        mob_no_exist = StudentModel.objects.filter(mob_no=mob_no,is_active=True).exclude(id=instance.pk).first()
        if mob_no_exist:
            raise serializers.ValidationError({"detail":"There is already an existing mobile number"})
        else:
            if city_extra:
                CityModel.objects.filter(id=instance.city.pk, is_active=True).update(**city_extra)
            if state_extra:
                StateModel.objects.filter(id=instance.state.pk, is_active=True).update(**state_extra)
            if country_extra:
                CountryModel.objects.filter(id=instance.country.pk, is_active=True).update(**country_extra)
            StudentModel.objects.filter(id=instance.pk,is_active=True).update(**validated_data)
            instance=StudentModel.objects.get(id=instance.pk)
            instance.save()
            return instance


    @staticmethod
    def get_city_data(obj):
        return obj.city.name if obj.city else None

    @staticmethod
    def get_state_data(obj):
        return obj.state.name if obj.state else None

    @staticmethod
    def get_country_data(obj):
        return obj.country.name if obj.country else None


class EventSerializer(ModelSerializer):
    class Meta:
        model = EventModel
        fields = '__all__'

class StudentParticipationSerializer(ModelSerializer):
    student = StudentSerializer(required=True)
    event = EventSerializer(required=True)
    class Meta:
        model = StudentParticipationModel
        fields = '__all__'

    def create(self,validated_data):
        student = validated_data.pop('user',None)
        event = validated_data.pop('event',None)
        student_data = StudentModel.objects.filter(student_id=student['student_id']).first()
        event_data = EventModel.objects.filter(id=event['id']).first()
        if student_data.exists() and event_data.exists():
            instance = StudentParticipationModel.objects.create(**validated_data)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError({"details":"Event or Student don't exist"})







