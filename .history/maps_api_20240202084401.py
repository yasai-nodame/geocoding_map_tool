from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import OpenCage
import folium

#緯度、経度から住所を検索　今回は必要ないかも
# def address_get(latitude,longitude):
# #geocoderのapiキー
#     api_key = '1ed415b65ba44d98aa3c6f61861aeb83'
#     geolocator = OpenCage(api_key)

#     latitude = latitude
#     longitude = longitude

#     location = geolocator.reverse((latitude, longitude),language='ja')

#     if location:
#         print(location.address)
#     else:
#         print('ジオコーディングができませんでした')

folium_map = folium.Map(location=[35.69389, 139.703613], zoom_start=15)

folium_map