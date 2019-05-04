
from rest_framework import serializers

from api.models import Attendees, Address, EventTypes, Events, Employees, ShowmanHouse, Country, City, FeeSchedule, FederativeRepublic, PaymentMethod, EntertainingGroup, AdministrativeStuff, Discount

from django.contrib.auth.models import User


class AttendeesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    second_name = serializers.CharField(required=True)

    def create(self, validated_data):
        attendees = Attendees(**validated_data)
        attendees.save()
        return attendees

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Address
        fields = ('id', 'district', 'street', 'apartments',)


class DiscountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Discount
        fields = ('id', 'orders_number', 'discount',)


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    country_name = serializers.CharField(required=True)

    def create(self, validated_data):
        attendees = Attendees(**validated_data)
        attendees.save()
        return attendees

    def update(self, instance, validated_data):
        instance.country_name = validated_data.get('country_name', instance.country_name)
        instance.save()
        return instance