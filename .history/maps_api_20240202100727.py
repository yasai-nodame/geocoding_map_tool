from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import OpenCage
import folium
from folium import Circle
import main

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

def latitude_longitude(longitude_latitude_list):
    folium_map = folium.Map(location=[longitude_latitude_list[1], longitude_latitude_list[0]], zoom_start=12)
    
    #半径をメートルに変換(1km = 1000メートル)
    radius_meters = 10 * 1000

    # folium.Marker(location=[longitude_latitude_list[1], longitude_latitude_list[0]],radius=500).add_to(folium_map)
    
    #半径10km内をサークルで色付け
    Circle(
        location=[longitude_latitude_list[1], longitude_latitude_list[0]],
        radius=radius_meters,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.2
    ).add_to(folium_map)

    folium_map.save("map.html")

latitude_longitude(main.latitude_longitude())
