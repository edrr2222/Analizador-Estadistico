from django.urls import path
from . import views

urlpatterns = [
    path('', views.star ,name = '' ),
    path('admin', views.admin,name='admin'),
    path('formulario', views.formulario ,name = 'formulario' ),
    path('consultar_solicitud', views.consultar_solicitud, name='consultar_solicitud'),
]