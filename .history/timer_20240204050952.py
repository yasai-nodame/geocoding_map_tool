import requests 
import pandas as pd

def restaurant_to_dataframe():
    api_key = 'zuJW6Y1645BXlaPo1Z0P2ekxlMahfuUEhMGXezgQR3MNSWZHmxhu3k2OuwJO9yakEJ9gs-WB8_k6n4fLW2m1Nk5Zl5CLDJCBOzH07kCWOjEh394Cv4_o86X_Q42-ZXYx'

    url = 'https://api.yelp.com/v3/businesses/search'

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
    
    df.to_csv('Restaurant.csv')


restaurant_to_dataframe()
