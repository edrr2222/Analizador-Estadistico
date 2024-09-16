from django.db import models

# Create your models here.
class Info_banco(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente	= models.IntegerField()
    genero = models.IntegerField()
    edad_anios = models.IntegerField()
    codigo_ciudad_residencia = models.CharField(max_length=100)
    nombre_ciudad_residencia = models.CharField(max_length=100)
    nro_prestamos_recibidos	= models.IntegerField()
    endeudamiento_sistema_financiero = models.FloatField()
    saldo_creditos = models.FloatField()
    saldo_ahorro = models.FloatField()
    saldo_cdt = models.FloatField()
    excedentes_negocio = models.FloatField()
    antiguedad_laboral_anios = models.IntegerField()
    integrantes_hogar = models.IntegerField()
    dias_mora_credito = models.IntegerField()    