
from rest_framework import serializers

from api.models import Attendees1, Address1, EventTypes1, OurEvents1, Employees1, ShowmanHouse1, Country1, City1, FeeSchedule1, FederativeRepublic1, PaymentMethod1, EntertainingGroup1, AdministrativeStuff1, Discount1

from django.contrib.auth.models import User


class AttendeesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    second_name = serializers.CharField(required=True)

    def create(self, validated_data):
        attendees = Attendees1(**validated_data)
        attendees.save()
        return attendees

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.save()
        return instance


class EventTypesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    event_title = serializers.CharField(required=True)
    event_description = serializers.CharField(required=True)

    def create(self, validated_data):
        events = EventTypes1(**validated_data)
        events.save()
        return events

    def update(self, instance, validated_data):
        instance.event_title = validated_data.get('event_title', instance.event_title)
        instance.event_description = validated_data.get('event_description', instance.event_description)
        instance.save()
        return instance


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Address1
        fields = ('id', 'district', 'street', 'apartments',)


class DiscountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Discount1
        fields = ('id', 'orders_number', 'discount',)


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    country_name = serializers.CharField(required=True)

    def create(self, validated_data):
        attendees = Attendees1(**validated_data)
        attendees.save()
        return attendees

    def update(self, instance, validated_data):
        instance.country_name = validated_data.get('country_name', instance.country_name)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ('id', 'username', 'email',)