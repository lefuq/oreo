from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Addressee, Mail, Phone
from .serializers import AddresseeSerial, PhoneSerial, MailSerial
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class AddresseeViewSet(viewsets.ModelViewSet):
    queryset = Addressee.objects.all()
    serializer_class = AddresseeSerial
    filter_backends = [OrderingFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        msg = 'User {} created object Addressee (id={})'.format(
            request.user,
            serializer.data["id"])
        if 'phone.phone_type' in request.data:
            msg += ' and related Phone object'
        if 'mail.mail_type' in request.data:
            msg += ' and related Mail object'
        logger.warning(msg)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        msg = 'User {} updated object Addressee (id={}) with next properties: {}'.format(
            request.user,
            instance.id,
            ', '.join([i for i in request.data])
            )
        logger.warning(msg)
        return self.update(request, *args, **kwargs)


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerial
    filter_backends = [OrderingFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        msg = 'User {} created object Mail (id={}) for Addresse(id={})'.format(
            request.user,
            serializer.data["id"],
            serializer.data["user_id"])
        logger.warning(msg)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        msg = 'User {} updated object Mail (id={}) with next properties: {}'.format(
            request.user,
            instance.id,
            ', '.join([i for i in request.data])
            )
        logger.warning(msg)
        return self.update(request, *args, **kwargs)


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerial
    filter_backends = [OrderingFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        msg = 'User {} created object Phone (id={}) for Addresse(id={})'.format(
            request.user,
            serializer.data["id"],
            serializer.data["user_id"])
        logger.warning(msg)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        msg = 'User {} updated object Phone (id={}) with next properties: {}'.format(
            request.user,
            instance.id,
            ', '.join([i for i in request.data])
            )
        logger.warning(msg)
        return self.update(request, *args, **kwargs)
