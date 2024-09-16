from django.http import JsonResponse
from .models import Info_banco
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from difflib import SequenceMatcher

def determinar_credito(request, datos_formulario):
    
    dias_mora_credito = int(datos_formulario.get('dias_mora_credito'))
    integrantes_hogar = int(datos_formulario.get('integrantes_hogar'))
    antiguedad_laboral_anios = int(datos_formulario.get('antiguedad_laboral_anios'))
    saldo_creditos = int(datos_formulario.get('saldo_creditos'))
    saldo_ahorro = int(datos_formulario.get('saldo_ahorro'))
    nro_prestamos_recibidos = int(datos_formulario.get('nro_prestamos_recibidos'))
    edad_anios = int(datos_formulario.get('edad_anios'))

    nombre_ciudad_residencia = datos_formulario.get('nombre_ciudad_residencia')
    genero = datos_formulario.get('genero')
    
    # Obtener los datos de la base de datos
    data = Info_banco.objects.values('genero', 'edad_anios', 'nro_prestamos_recibidos', 'saldo_creditos', 'saldo_ahorro', 'antiguedad_laboral_anios', 'integrantes_hogar', 'dias_mora_credito')

    # Convertir los datos en un DataFrame de pandas
    df = pd.DataFrame(data)

    # Realizar la ingeniería de características para ajustar la importancia de ciertos parámetros
    # Aquí puedes ajustar los pesos de las características o eliminar aquellas que consideres menos importantes

    # Aquí se asume que 'saldo_ahorro' y 'antiguedad_laboral_anios' tienen una mayor importancia


    #df['saldo_ahorro'] = df['saldo_ahorro'] * 3
    #df['edad_anios'] = df['edad_anios'] * 2
    #df['antiguedad_laboral_anios'] = df['antiguedad_laboral_anios'] * 1.5
    #df['dias_mora_credito'] = 1 / (df['dias_mora_credito'] + 1)
    #df['integrantes_hogar'] = 1 / (df['integrantes_hogar'] + 1)


    # Crear el modelo de regresión lineal
    model = LinearRegression()
    X = df.drop('dias_mora_credito', axis=1)
    y = df['dias_mora_credito']
    model.fit(X, y)

    # Preparar los datos de entrada para la predicción
    input_data = [genero, edad_anios, nro_prestamos_recibidos, saldo_creditos, saldo_ahorro, antiguedad_laboral_anios, integrantes_hogar]
    print(input_data)
    # Realizar la predicción
    prediction = model.predict([input_data])

    # Determinar la viabilidad de dar un crédito
    if prediction[0] < 0:
        resultado = "Aprobado"
    else:
        valido = 1
        if dias_mora_credito == 0 and integrantes_hogar <= 1 and antiguedad_laboral_anios >= 2 and saldo_creditos < saldo_ahorro and nro_prestamos_recibidos >= 1 and ((edad_anios >= 22 and edad_anios <= 25) or edad_anios >= 74) and ((SequenceMatcher(None, 'CUCUTA', nombre_ciudad_residencia).ratio())>0.8 or (SequenceMatcher(None, 'MEDELLIN', nombre_ciudad_residencia).ratio())>0.8 or (SequenceMatcher(None, 'BOGOTA', nombre_ciudad_residencia).ratio())>0.8 or (SequenceMatcher(None, 'ALVARADO', nombre_ciudad_residencia).ratio())>0.8 ):
            valido = 1
        else:
            valido = 0

        if valido == 1:
            resultado = "Aprobado"
        else:
            resultado = "Rechazado"
        

    return resultado
