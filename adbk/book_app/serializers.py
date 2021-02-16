from rest_framework import serializers
from .models import Addressee, Mail, Phone
import logging


logger = logging.getLogger(__name__)


class MailSerial(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'


class NestedMailSerial(serializers.ModelSerializer):
    class Meta:
        model = Mail
        exclude = ['user_id']


class PhoneSerial(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class NestedPhoneSerial(serializers.ModelSerializer):
    class Meta:
        model = Phone
        exclude = ['user_id']


class AddresseeSerial(serializers.ModelSerializer):
    mail = NestedMailSerial(required=False)
    phone = NestedPhoneSerial(required=False)
    birth = serializers.DateField(
        format='%d-%m-%Y',
        input_formats=['%d-%m-%Y', 'iso-8601'])

    class Meta:
        model = Addressee
        fields = '__all__'

    def create(self, validated_data):
        if 'mail' not in validated_data:
            mail_data = None
        else:
            mail_data = validated_data.pop('mail')
        if 'phone' not in validated_data:
            phone_data = None
        else:
            phone_data = validated_data.pop('phone')
        addressee = Addressee.objects.create(**validated_data)
        if mail_data:
            Mail.objects.create(user_id=addressee, **mail_data)
        if phone_data:
            Phone.objects.create(user_id=addressee, **phone_data)
        return addressee
