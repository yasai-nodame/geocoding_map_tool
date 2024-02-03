import requests 
import time

#ジオコーディングは住所を座標に変換する。 逆ジオコーディングは座標を住所に変換する。
def get_nearby_places(address,radius_km=10):
    
    for i in range(1,100):
        time_limit = i
    
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
            'limit': 10
        }
        
        float_latitude = float(latitude) #floatにキャッチする
        float_longitude = float(longitude)
        
        for i in range(100):
            
            #微小に座標を変化させる
            offset_lat = (2 * (0.5 - i / 10)) * (radius_km / 110.574) #1度あたり約110.574km
            offset_lon = (2 * (0.5 - i / 10)) * (radius_km / (111.32 * abs(float_latitude))) #緯度による経度の変化
            
            current_lat = float_latitude + offset_lat 
            current_lon = float_longitude + offset_lon 
            
            # print(current_lat)
            # print(current_lon)
            
            reverse_params = {
                'format': 'json',
                'lat': current_lat,
                'lon': current_lon,
                'radius': radius_km * 1000,
                'limit': 1
            }
            
            reverse_response = requests.get(nominatim_url,params=reverse_params)
            
            if reverse_response.status_code == 200:
                place = reverse_response.json()[0]
            else:
                print(f'Error in reverse geocoding attempt{i + 1}.')
            
            time.sleep(1)
        else:
            print('Error in geocoding')
            # print(reverse_response.json())
        
get_nearby_places('東京都新宿区')