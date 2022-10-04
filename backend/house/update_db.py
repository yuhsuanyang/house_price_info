import pandas as pd
from crawl import get_query_cmd, query_house, get_house_group
from .config import section
from .models import House, Community

args = {
    'city': '台北市',
    'section': [sec for sec in section['台北市'] if sec != '萬華區'],
    'pattern': [1, 3],   
    'houseage': [0, 20],
}
def main(args):
    cluster_id_start = len(Community.objects.all())
    query_cmd = get_query_cmd(args)
    houses = query_house(query_cmd)
    clusters =  get_house_group(houses, cluster_id_start)
    houses = pd.concat(clusters)
    for i in range(len(houses)):
        row = House(
                id=houses[i]['houseid'],
                cluster_id=houses.iloc[i]['cluster'],
                shape_name=houses.iloc[i]['shape_name'],
                region_name=houses.iloc[i]['region_name'],
                section=houses.iloc[i]['section_name'],
                address=houses.iloc[i]['address'],
                location=houses.iloc[i][''],
                price=houses.iloc[i]['price'],
                unit_price=houses.iloc[i]['unitprice'],
                rooms=houses.iloc[i]['room'],
                age=houses.iloc[i]['houseage'],
                floor=houses.iloc[i]['floor'],
                main_area=houses.iloc[i]['mainarea'],
                community_id=houses.iloc[i]['community_link'],
                tag=houses.iloc[i]['tag'])

