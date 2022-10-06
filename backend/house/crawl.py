import time
import random
import requests
import numpy as np
import pandas as pd
from .config import regionid, section
from bs4 import BeautifulSoup

HEADER = {
    'user-agent':
    'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
'''
query_args example:
{
    'city': '台北市',
    'section': ['內湖區'],
    'area': [20, 30], # 物件面積
    'pattern': [2], # 格局(n房), n=1~6
    'houseage': [0, 20],
    'price': [1000, 2000]
}
'''


def get_query_cmd(args):
    query_cmd = f"regionid={regionid[args['city']]}&"
    for arg in args:
        if arg == 'city':
            continue
        query_cmd += f"{arg}="
        if arg in ['section', 'pattern']:
            for option in args[arg]:
                if arg == 'section':
                    query_cmd += f"{section[args['city']][option]},"
                elif arg == 'pattern':
                    query_cmd += f"{option},"
            query_cmd = query_cmd[:-1] + '&'
        elif arg in ['houseage', 'price']:
            query_cmd += f"{args[arg][0]}$_{args[arg][1]}$&"
        elif arg == 'area':
            query_cmd += f"{args[arg][0]}_{args[arg][1]}&"
    query_cmd = query_cmd[:-1]
    return query_cmd


def download_house_data(query_cmd, page):
    s = requests.Session()
    url = 'https://sale.591.com.tw/'
    r = s.get(url, headers=HEADER)
    soup = BeautifulSoup(r.text, 'html.parser')
    token_item = soup.select_one('meta[name="csrf-token"]')
    HEADER['X-CSRF-TOKEN'] = token_item['content']
    res = s.get(
        f'https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=3&{query_cmd}&firstRow={page * 30}',
        headers=HEADER)
    if res.status_code == 200:
        data = res.json()['data']['house_list']
        print(f'success, {len(data)} items found')
        return data
    else:
        print(f'fail, status code: {res.status_code}')
        return False


def query_house(query_cmd):
    status = True
    page = 0
    results = []
    while status:
        data = download_house_data(query_cmd, page)
        if not data:
            status = False
        else:
            results += data
            print('sleeping...')
            time.sleep(random.uniform(2, 5))
            page += 1
    df = []
    columns = [
        'houseid', 'title', 'shape_name', 'region_name', 'section_name',
        'address', 'price', 'unitprice', 'houseage', 'room', 'floor', 'area',
        'mainarea', 'community_name', 'community_link', 'tag'
    ]
    for item in results:
        row = []
        for col in columns:
            if col in item:
                row.append(item[col])
            else:
                row.append(np.nan)
        df.append(row)
    df = pd.DataFrame(df, columns=columns)
    null_cols = ['community_link', 'tag']
    non_null_cols = [col for col in columns if col not in null_cols]
    return df.dropna(subset=non_null_cols)


def get_house_group(df, cluster_id_start):
    groups = []
    i = 0
    for _, df_group in df.groupby(by=['community_link', 'floor', 'price']):
        df_group['cluster'] = cluster_id_start + i
        groups.append(df_group)
        i += 1
    print(len(groups))
    return groups


def download_real_price(community_link):
    #    url = f'https://market.591.com.tw/{community_id}/price'
    s = requests.Session()
    res = s.get(f"{community_link}/price", headers=HEADER)
    soup = BeautifulSoup(res.text, 'html.parser')
    realprice_records = soup.find_all('section', class_='realprice-list-row')
    print(len(realprice_records))
    cols = ['year-month', 'floor', 'house-total', 'park']
    records = []
    for i in range(len(realprice_records)):
        record = []
        for col in cols:
            if col == 'house-total' or col == 'park':
                record.extend(
                    realprice_records[i].find(class_=col).text.split('萬'))
            else:
                record.append(realprice_records[i].find(class_=col).text)


#        record.append(realprice_records[i].find('address').text)
        records.append(record)
    records = pd.DataFrame(
        records, columns=['交易年月', '樓層', '房屋總價', '面積格局', '車位總價', '車位面積'])
    return records


def download_imgs(house_id, save_path=None):
    url = f'https://sale.591.com.tw/home/house/detail/2/{house_id}.html'
    s = requests.Session()
    res = s.get(url, headers=HEADER)
    soup = BeautifulSoup(res.text, 'html.parser')
    img_urls = [
        img_tag['data-original']
        for img_tag in soup.find_all(class_='pic-box-img')
    ]
    print(f"{len(img_urls)} imgs")
    for i, url in enumerate(img_urls):
        res = requests.get(url)
        if save_path:
            with open(f"{save_path}/{house_id}_{i}.jpg",
                      "wb") as file:  # 開啟資料夾及命名圖片檔
                file.write(res.content)
    return img_urls


def download_iframe(house_id):
    url = f'https://sale.591.com.tw/home/house/detail/2/{house_id}.html'
    s = requests.Session()
    res = s.get(url, headers=HEADER)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.find('iframe', id='detail-map-free')['src']
