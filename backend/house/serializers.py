from rest_framework import serializers
from .models import House


class ClusterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = House
        fields = [
            'id', 'title', 'shape_name', 'region_name', 'section_name',
            'address', 'location', 'price', 'unit_price', 'rooms', 'age',
            'floor', 'area', 'main_area', 'community_id', 'tag'
        ]
