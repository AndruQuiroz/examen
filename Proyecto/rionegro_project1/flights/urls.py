# flights/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL para la zona de inicio (este paso)
    path('', views.inicio, name='inicio'),
    
    # URLs para los próximos pasos (las agregamos ahora para que los enlaces funcionen)
    path('registrar/', views.registrar_vuelo, name='registrar_vuelo'),
    path('listar/', views.listar_vuelos, name='listar_vuelos'),
    path('estadisticas/', views.estadisticas_vuelos, name='estadisticas_vuelos'),
]