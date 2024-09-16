from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Info_banco
from .logic import determinar_credito
from django.http import HttpResponseRedirect
from datetime import datetime
# Create your views here.

def admin(request):
    info_banco = Info_banco.objects.all()
    return render(request,'ShowAdminData/index.html',{"DataBanco": info_banco })

def star(request):
    return render(request,'paginas/formulario.html')

def formulario(request):
    return render(request,'paginas/formulario.html')

def consultar_solicitud(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        genero = request.POST.get('optGenero')
        nombre_ciudad_residencia = request.POST.get('txtCiudadRecidencia')
        saldo_creditos = request.POST.get('txtSaldoCredito')
        saldo_ahorro = request.POST.get('txtSaldoAhorro')
        integrantes_hogar = request.POST.get('txtIntegrantesHogar')
        dias_mora_credito = request.POST.get('txtDiasMora')
        nro_prestamos_recibidos = request.POST.get('txtNumeroPrestamo')

        fecha_nacimiento_str = request.POST.get('txtFechaNacimiento')
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
        edad_anios = calcular_edad(fecha_nacimiento)

        fecha_laboral_str = request.POST.get('txtFechaInicioEmpresa')
        fecha_laboral = datetime.strptime(fecha_laboral_str, '%Y-%m-%d').date()
        antiguedad_laboral_anios = calcular_edad(fecha_laboral)
        
        datos_formulario = {
            'nombre': nombre,
            'genero': genero,
            'edad_anios': edad_anios,
            'nombre_ciudad_residencia': nombre_ciudad_residencia,
            'nro_prestamos_recibidos': nro_prestamos_recibidos,
            'saldo_creditos': saldo_creditos,
            'saldo_ahorro': saldo_ahorro,
            'antiguedad_laboral_anios': antiguedad_laboral_anios,
            'integrantes_hogar': integrantes_hogar,
            'dias_mora_credito': dias_mora_credito,
        }
        resultado = determinar_credito(request, datos_formulario)
        detalle = nombre+" Gracias por utilizar nuestro software. ¡Bien hecho!"
        return render(request, 'paginas/resultados.html', {"resultado": resultado,"detalle":detalle})
    else:
        return render(request, 'paginas/formulario.html')

def calcular_edad(fecha_nacimiento):
    today = datetime.today()
    age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return age