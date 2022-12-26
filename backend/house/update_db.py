import pandas as pd
import multiprocessing as mp
from tqdm import tqdm
from .crawl import get_query_cmd, query_house, get_house_group, download_iframe, download_imgs
from .config import section
from .models import House, Community, HouseImg

args = {
    'city': '台北市',
    'section': [sec for sec in section['台北市'] if sec != '萬華區'],
    'pattern': [1, 3],
    'houseage': [0, 20],
}

mp.set_start_method('fork')


def get_data(args):
    query_cmd = get_query_cmd(args)
    houses = query_house(query_cmd)
    houses['community_link'] = houses['community_link'].apply(
        lambda x: x.split('/')[-1])
    houses['houseid'] = houses['houseid'].astype(str)
    houses.drop_duplicates(subset=['houseid'], inplace=True)
    community = houses[['community_name', 'community_link']].drop_duplicates()
    return houses, community


def add_house(houses):
    for i in tqdm(range(len(houses))):
        house_id = houses.iloc[i]['houseid']
        try:
            iframe_url = download_iframe(house_id)
        except:
            print('iframe download fail')
            continue
        tag = ','.join(houses.iloc[i]['tag'])
        row = House(id=house_id,
                    cluster_id=houses.iloc[i]['cluster'],
                    title=houses.iloc[i]['title'],
                    shape_name=houses.iloc[i]['shape_name'],
                    region_name=houses.iloc[i]['region_name'],
                    section_name=houses.iloc[i]['section_name'],
                    address=houses.iloc[i]['address'],
                    location=iframe_url,
                    price=houses.iloc[i]['price'],
                    unit_price=houses.iloc[i]['unitprice'],
                    rooms=houses.iloc[i]['room'],
                    age=houses.iloc[i]['houseage'],
                    floor=houses.iloc[i]['floor'],
                    area=houses.iloc[i]['area'],
                    main_area=houses.iloc[i]['mainarea'],
                    community_id=houses.iloc[i]['community_link'],
                    tag=tag)
        row.save()


def add_community(community):
    for i in tqdm(range(len(community))):
        row = Community(id=community.iloc[i]['community_link'],
                        name=community.iloc[i]['community_name'])
        row.save()


def add_img(houseid, img_list):
    for url in img_list:
        row = HouseImg(house_id=houseid, img_url=url)
        row.save()


def get_gallery(houseid):
    imgs = download_imgs(houseid)
    if not len(imgs):
        return [houseid]
    else:
        add_img(houseid, imgs)
        return []


def house2df():
    data = House.objects.all()
    if len(data):
        columns = list(data[0].get_basic_info().keys())
        df = []
        for row in data:
            df.append(list(row.get_basic_info().values()))
        df = pd.DataFrame(df, columns=columns)
    else:
        df = pd.DataFrame({'houseid': []})
    return df


def get_exist_cluster(previous, new):
    new_cluster = []
    for i in range(len(new)):
        house_id = new['houseid'].iloc[i]
        community = new['community_link'].iloc[i]
        if not len(community):
            continue
        floor = new['floor'].iloc[i]
        price = new['price'].iloc[i]
        exist_cluster = previous[(previous['community_link'] == community)
                                 & (previous['floor'] == floor) &
                                 (previous['price'] == price)]
        if len(exist_cluster):
            new_cluster.append(
                [house_id, exist_cluster['cluster_id'].mode().iloc[0]])
    return pd.DataFrame(new_cluster, columns=['houseid',
                                              'cluster']).drop_duplicates()


def delete():
    House.objects.all().delete()
    HouseImg.objects.all().delete()
    Community.objects.all().delete()


def main(args):
    previous_houses = house2df()
    houses, community = get_data(args)
    new_houses = houses[~houses['houseid'].isin(previous_houses['houseid'])]
    if len(previous_houses):
        new_cluster = get_exist_cluster(previous_houses, new_houses)
        new_houses = new_houses.merge(new_cluster, how='left')
        new_houses_without_cluster = new_houses[new_houses['cluster'].isnull()]
        new_houses_with_cluster = new_houses[~new_houses['cluster'].isnull()]
    else:
        new_houses_without_cluster = new_houses
        new_houses_with_cluster = pd.DataFrame()  # empty

    cluster_id_start = len(House.objects.values('cluster_id').distinct())
    new_clusters = get_house_group(new_houses_without_cluster,
                                   cluster_id_start)
    new_houses_without_cluster = pd.concat(new_clusters)
    houses = pd.concat([new_houses_without_cluster, new_houses_with_cluster])
    work_load = houses['houseid'].values.tolist()
    with mp.Pool(20) as p:
        no_img = list(
            tqdm(p.imap(get_gallery, work_load), total=len(work_load)))
    no_img = sum(no_img, [])
    print(no_img, 'no imgs')
    houses = houses[~houses['houseid'].isin(no_img)]
    add_house(houses)  # need speed up
    add_community(community)


## TODO ##
# merge get_gallery and download_iframe into one function
