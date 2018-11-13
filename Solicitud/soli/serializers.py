from .models import Solicitud
from rest_framework import serializers


class SolicitudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('correo', 'tipoSolicitud', 'motivo', 'gps')

