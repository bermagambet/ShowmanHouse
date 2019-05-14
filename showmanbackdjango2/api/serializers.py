
from rest_framework import serializers

from api.models import Attendees1, Address1, EventTypes1, OurEvents1, Employees1, ShowmanHouse1, Country1,\
    City1, FeeSchedule1, FederativeRepublic1, PaymentMethod1, EntertainingGroup1, Avatars1,\
    AdministrativeStuff1, Discount1, Orders1, Avatars1Events


from django.contrib.auth.models import User


class EmployeesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = Employees1
        fields = ('id', 'first_name', 'second_name', 'position', 'phone_number', 'department_id')

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


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatars1
        fields = ('id', 'avatar', 'customer_id')



class EventAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatars1Events
        fields = ('id', 'avatar', 'event_id')

class OurEventsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = OurEvents1
        fields = ('id', 'start_date', 'end_date', 'participants', 'price', 'type_id', 'payment_id')


class EventTypesSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',)

class OrdersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = Orders1
        fields = ('id', 'event_id', 'department_id', 'customer_id')


class ShowmanHouseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ShowmanHouse1
        fields = ('id', 'employees_number', 'event_id',)

class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


    class Meta:
        model = Address1
        fields = ('id', 'district', 'street', 'apartments', 'city_id', 'customer_id')

class CitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = City1
        fields = ('id', 'city_name', 'city_state', 'country_id')


class DiscountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Discount1
        fields = ('id', 'orders_number', 'discount', 'customer_id')


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    country_name = serializers.CharField(required=True)

    def create(self, validated_data):
        attendees = Country1(**validated_data)
        attendees.save()
        return attendees

    def update(self, instance, validated_data):
        instance.country_name = validated_data.get('country_name', instance.country_name)
        instance.save()
        return instance


class PaymentMethodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PaymentMethod1
        fields = ('id', 'method_name', 'payment_id',)


class FeeScheduleSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(required=True)

        class Meta:
            model = FeeSchedule1
            fields = ('id', 'payment_date', 'payment_amount', 'created_by')
