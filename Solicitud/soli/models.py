from django.db import models


class Solicitud(models.Model):

    correo = models.CharField(max_length=100, null=False)
    tipoSolicitud = models.CharField(max_length=100, null=False)
    motivo = models.CharField(max_length=10000, null=False)
    gps = models.CharField(max_length=300)
