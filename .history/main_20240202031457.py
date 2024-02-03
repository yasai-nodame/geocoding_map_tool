import requests 
from requests.exceptions import HTTPError, RequestException, JSONDecodeError

def search_osm_places(latitude, longitude, radius, amenity):
    overpass_url = "https://lz4.overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    node(around:{radius},{latitude},{longitude})["amenity"="{amenity}"]
    out body;
    """
    try:
        response = requests.post(overpass_url,data=query)
        data = response.json()
        return data 
    except JSONDecodeError:
        print('JSONデコードエラー: 有効なJSONデータが取得できませんでした')
        return None 
    except HTTPError as http_err:
        print(f'HTTPエラーが発生しました: {http_err}')
        return None
    except RequestException as req_err:
        print(f'リクエストエラーが発生しました: {req_err}')
        return None

results = search_osm_places(40.7128,-74.006, 1000, 'restaurant')
if results is not None:
    print(results)