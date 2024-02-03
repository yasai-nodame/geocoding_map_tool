import requests 
from requests.exceptions import HTTPError, RequestException, JSONDecodeError
import xml.etree.ElementTree as ET 
import json

def search_osm_places(latitude, longitude, radius, amenity):
    overpass_url = "https://lz4.overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    node(around:{radius},{latitude},{longitude})["amenity"="{amenity}"]
    out body;
    """
    try:
        response = requests.post(overpass_url,data=query)
        response.raise_for_status()
        
        #XMLからJSONに変換
        root = ET.fromstring(response.text)
        json_data = json.dumps(xml_to_dict(root))
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

def xml_to_dict(element):
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child_data:
            result[child.tag] = child_data 
        else:
            result[child.tag] = child.text 
        return result

results = search_osm_places(40.7128,-74.006, 1000, 'restaurant')
if results is not None:
    print(results)