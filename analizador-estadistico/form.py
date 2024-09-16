from django import forms

class SolicitudForm(forms.Form):
    OptExampleSelect = forms.ChoiceField(choices=[('CC', 'CC')], label='Tipo de documento de identidad')
    txtNumeroDocumento = forms.IntegerField(label='Número de documento')
    txtNombre = forms.CharField(max_length=100, label='Nombre')
    txtEmail = forms.EmailField(label='Correo electrónico')
    txtFechaNacimiento = forms.DateField(label='Fecha de Nacimiento')
    optGenero = forms.ChoiceField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], label='Género')
    txtCiudadRecidencia = forms.CharField(max_length=100, label='Ciudad de Residencia')
    txtNumeroPrestamo = forms.IntegerField(label='Número Prestamos Recibidos')
    txtSaldoCredito = forms.IntegerField(label='Cual es su saldo total de sus creditos?')
    txtSaldoAhorro = forms.IntegerField(label='Cuanto Recuerda Aver Ahorrado?')
    txtFechaInicioEmpresa = forms.DateField(label='Fecha De Inicio En Su Empresa?')
    txtIntegrantesHogar = forms.IntegerField(label='Número de Integrantes en el Hogar')
    txtDiasMora = forms.IntegerField(label='Si Tienes Dias En Mora Indicanos Para Ayudarte!')