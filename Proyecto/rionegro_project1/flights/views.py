from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Flight
from .forms import FlightForm

# Vista para la página de inicio
def inicio(request):
    return render(request, 'flights/inicio.html')

# Vista para registrar un nuevo vuelo
def registrar_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
    else:
        form = FlightForm()
    
    return render(request, 'flights/registrar_vuelo.html', {'form': form})

# Vista para listar todos los vuelos (punto d)
def listar_vuelos(request):
    # Obtenemos todos los vuelos y los ordenamos por precio ascendente
    vuelos = Flight.objects.all().order_by('precio')
    return render(request, 'flights/listar_vuelos.html', {'vuelos': vuelos})

# Vista para mostrar las estadísticas (punto e)
def estadisticas_vuelos(request):
    # Contamos cuántos vuelos hay de cada tipo
    num_nacionales = Flight.objects.filter(tipo='Nacional').count()
    num_internacionales = Flight.objects.filter(tipo='Internacional').count()
    
    # Calculamos el precio promedio de los vuelos nacionales
    resultado_avg = Flight.objects.filter(tipo='Nacional').aggregate(promedio=Avg('precio'))
    # Si no hay vuelos nacionales, el promedio será 0 para evitar errores
    promedio_nacional = resultado_avg['promedio'] or 0
    
    context = {
        'num_nacionales': num_nacionales,
        'num_internacionales': num_internacionales,
        'promedio_nacional': promedio_nacional,
    }
    
    return render(request, 'flights/estadisticas.html', context)