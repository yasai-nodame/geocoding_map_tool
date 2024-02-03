import requests 

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

print(businesses['alias'])
print(businesses['image_url'])
print(businesses['url'])
print(businesses['location'])
print(businesses['zip_code'])
print(businesses['display_phone'])