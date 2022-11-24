from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .serializers import ClusterSerializer
from .models import House
from .config import section
from .selector import ItemSelector

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
        'num_rooms': '0' if data['rooms'] == '不限' else data['rooms'],
    }
    print(posted_args)
    selector = ItemSelector()
    for col in posted_args:
        if col in ['region_name', 'section_name']:
            print(col)
            selector.query_by_str(col, posted_args[col])
        elif col in ['price', 'area', 'houseage']:
            selector.query_by_range(col, posted_args[col][0],
                                    posted_args[col][1])
        else:
            selector.query_by_num(col, posted_args[col])
    print(selector.all_data)
    #    selector.all_data.to_csv('query_result.csv', index=False)
    return HttpResponse(400)
