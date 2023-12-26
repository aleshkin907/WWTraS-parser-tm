import requests
import time
import json
from configs.environment import get_env_variables

env = get_env_variables()
key = env.KEY

# get_list_items_info_url = f'https://market.csgo.com/api/v2/get-list-items-info?key={key}&list_hash_name[]=AK-47 | Baroque Purple (Factory New)&list_hash_name[]=1st Lieutenant Farlow | SWAT'


def get_list_items_info(url: str, params: dict) -> dict:
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            items_info = response.json()
            return items_info
        except requests.RequestsJSONDecodeError as e:
            print(e)
    else:
        print(response.status_code)
    # return items_info

def get_prices(url: str) -> list:
    response = requests.get(url)
    items = response.json()
    return items.get('items')

def get_prices_class_instance(url: str) -> dict:
    pass


prices_url = 'https://market.csgo.com/api/v2/prices/RUB.json'
info_url = 'https://market.csgo.com/api/v2/get-list-items-info'


items = get_prices(prices_url)

# url_params = {"key": key}
# item_list = []
# a = 0
# for item in items:
#         if a < 50:
#             item_list.append(item['market_hash_name'])
#             a+=1

# url_params = {"key": key, "list_hash_name[]" : item_list}

# list_items_info = get_list_items_info(info_url, url_params)



# print(list_items_info)

def get_items_data_history(url: str, items: list, key: str, param: str) -> list:
    items_data_history = {}

    hash_names = [item[param] for item in items]

    subarrays = [hash_names[i:i+50] for i in range(0, len(hash_names), 50)]

    # print(subarrays[0])

    for subarray in subarrays:
        url_params = get_url_params(subarray, key, 'key', 'list_hash_name[]')
        temp_items = get_list_items_info(url, url_params)
        time.sleep(20)
        items_data_history.update(temp_items["data"])

    
    # with open("data.json", "w") as f:
    #     json.dump(items_data_history, f)
    
    return items_data_history

     
def get_url_params(data: list, key: str, key_name: str, param_name: str) -> dict:
    url_params = {key_name: key, param_name : data}
    return url_params


# a = get_items_data_history(info_url, items, key, "market_hash_name")
         