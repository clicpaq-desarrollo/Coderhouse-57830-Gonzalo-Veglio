# from django.http import JsonResponse
# from .models import Localidad

# def localidades_por_provincia(request, provincia_id):
#     localidades = Localidad.objects.filter(provincia_id=provincia_id).values('id', 'localidad')
#     return JsonResponse(list(localidades), safe=False)
