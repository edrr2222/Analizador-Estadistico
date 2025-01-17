# Generated by Django 3.2.8 on 2023-10-11 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info_banco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.IntegerField()),
                ('genero', models.CharField(max_length=100)),
                ('edad_anios', models.IntegerField()),
                ('codigo_ciudad_residencia', models.CharField(max_length=100)),
                ('nombre_ciudad_residencia', models.CharField(max_length=100)),
                ('nro_prestamos_recibidos', models.IntegerField()),
                ('endeudamiento_sistema_financiero', models.FloatField()),
                ('saldo_creditos', models.FloatField()),
                ('saldo_ahorro', models.FloatField()),
                ('saldo_cdt', models.FloatField()),
                ('excedentes_negocio', models.FloatField()),
                ('antiguedad_laboral_anios', models.IntegerField()),
                ('integrantes_hogar', models.IntegerField()),
                ('dias_mora_credito', models.IntegerField()),
            ],
        ),
    ]
