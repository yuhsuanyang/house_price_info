from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import ClusterSerializer
from .models import House
from .config import section
#from .selector import Selector

# Create your views here.


@csrf_exempt
def get_cluster(request, cluster_id):
    data = House.objects.filter(cluster_id=cluster_id)
    serializer = ClusterSerializer(data, many=True)
    return JsonResponse(serializer.data,
                        safe=False,
                        json_dumps_params={
                            'ensure_ascii': False,
                            'indent': 2
                        })


@csrf_exempt
def get_section(request):
    #    print(request.method)
    city_sections = {city: list(section[city].keys()) for city in section}
    return JsonResponse(city_sections,
                        json_dumps_params={
                            'ensure_ascii': False,
                            'indent': 2
                        })


@csrf_exempt
def get_posted_query(request):
    data = JSONParser().parse(request)
    posted_args = {
        'region_name': data['region'],
        'section_name': data['section'],
        'price': [data['price_min'], data['price_max']],
        'area': [data['area_min'], data['area_max']],
        'houseage': [data['age_min'], data['age_max']],
        'num_rooms': data['rooms'],
    }
    print(posted_args)
    return HttpResponse(400)
