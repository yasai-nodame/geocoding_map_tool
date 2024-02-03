import requests 


def get_nearby_places(address,radius_km=10):
    nominatim_url = 'https://nominatim.openstreetmap.org/search'

    goecode_params = {
        'q':address,
        'format':'json',
        'limit':1
    }

    response = requests.get(nominatim_url, params=goecode_params)
    
    if response.status_code == 200:
        location = response.json()[0]
        latitude = location['lat']
        longitude = location['lon']
    
    print(f'latitude:{latitude} longitude:{longitude}')

get_nearby_places('東京都新宿区')