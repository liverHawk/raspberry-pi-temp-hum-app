from django.shortcuts import render
from .measure import get_temp_hum

def index(request):
    return render(request, 'measure/index.html')

async def measure(request):
    time, temperature, humidity = get_temp_hum()
    context = {
        'time': time,
        'temperature': temperature,
        'humidity': humidity,
    }
    return render(request, 'measure/measure.html', context)
