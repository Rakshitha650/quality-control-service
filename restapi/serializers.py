from rest_framework import serializers
from .models import Clinic, Department, Equipments, EquipmentDetails, Parameters


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields = '__all__'


class EquipmentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentDetails
        fields = '__all__'

class ParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = '__all__'

