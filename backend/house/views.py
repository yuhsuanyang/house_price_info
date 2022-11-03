from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
def get_section(requsest):
    city_sections = {city: list(section[city].keys()) for city in section}
    return JsonResponse(city_sections,
                        json_dumps_params={
                            'ensure_ascii': False,
                            'indent': 2
                        })


def get_posted_query(request):
    posted_args = {
        'region_name': request.POST[''],
        'section_name': request.POST[''],
        'price': request.POST[''],
        'area': request.POST[''],
        'houseage': request.POST[''],
        'num_rooms': request.POST[''],
    }
    print(posted_args)
