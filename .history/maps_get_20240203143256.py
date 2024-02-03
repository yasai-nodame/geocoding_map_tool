import requests 


def get_nearby_places(address,radius_km=10):
    url = 'https://nominatim.openstreetmap.org/search'

    goecode_params = {
        'q':address,
        'format':'json',
        'limit':1
    }