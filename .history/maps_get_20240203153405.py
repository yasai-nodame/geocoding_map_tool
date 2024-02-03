import requests 

#ジオコーディングは住所を座標に変換する。 逆ジオコーディングは座標を住所に変換する。
def get_nearby_places(address,radius_km=10):
    nominatim_url = 'https://nominatim.openstreetmap.org/search'

    goecode_params = {
        'q':address,
        'format':'json',
        'limit':1
    }

    response = requests.get(nominatim_url, params=goecode_params)
    
    if response.status_code == 200:
        location = response.json()[0] #リストに内包されている辞書オブジェクト[0]を取得　jsonオブジェクトは辞書型で返される。
        latitude = location['lat'] #辞書のキーlatを取得
        longitude = location['lon'] #辞書のキーlonを取得
    
        #10km以内の地名を逆ジオコーディング
        reverse_params = {
            'format': 'json',
            'lat': latitude,
            'lon': longitude,
            'radius': radius_km * 1000, #メートル単位で指定
            'limit':100
        }

        resposne = requests.get(nominatim_url, params=reverse_params)
        print(response.json())
        
        
get_nearby_places('東京都新宿区')