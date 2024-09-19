from django.http import JsonResponse
from django.db.models import Sum
from envios.models import Envio
from django.db.models import Count
from django.shortcuts import render

def datos_envios_por_cliente(request):
    envios_por_cliente = Envio.objects.values('cliente__nombre').annotate(total_envios=Count('id'))
    data = {
        'labels': [envio['cliente__nombre'] for envio in envios_por_cliente],
        'values': [envio['total_envios'] for envio in envios_por_cliente],
    }
    return JsonResponse(data)



def datos_kilos_por_cliente(request):
    kilos_por_cliente = Envio.objects.values('cliente__nombre').annotate(total_kilos=Sum('productos__peso'))
    data = {
        'labels': [envio['cliente__nombre'] for envio in kilos_por_cliente],
        'values': [envio['total_kilos'] for envio in kilos_por_cliente],
    }
    return JsonResponse(data)


def mostrar_graficos(request):
    return render(request, 'graficos/mostrar_graficos.html')