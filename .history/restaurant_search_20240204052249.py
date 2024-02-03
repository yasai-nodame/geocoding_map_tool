import requests 
import pandas as pd
import configparser

def restaurant_to_dataframe():
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config.get('Section1','API_KEY')

    url = config.get('Section1','URL')

    params = {
        'latitude': 35.69389,
        'longitude': 139.703613,
        'radius': 10000
    }

    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(url,params=params,headers=headers)
    businesses = response.json()['businesses']

    
    alias_list = []
    image_url_list = []
    url_list = []
    address_list = []
    zip_code_list = []
    phone_list = []
    data_list = []

    for business in businesses:
        alias_list.append(business['alias'])
        image_url_list.append(business['image_url'])
        url_list.append(business['url'])
        address_list.append(business['location']['address1']+business['location']['address2'])
        zip_code_list.append(business['location']['zip_code'])
        phone_list.append(business['display_phone'])

    data_list.append(alias_list)
    data_list.append(image_url_list)
    data_list.append(url_list)
    data_list.append(address_list)
    data_list.append(zip_code_list)
    data_list.append(phone_list)
    
    columns = ['Restaurant_Name','Image_URL','Restaurant_URL','Address','Postal_Code','Phone']
    
    df = pd.DataFrame(data_list).T
    df.columns = columns
    
    # df.to_csv('Restaurant.csv')
    print(data_list)

restaurant_to_dataframe()
