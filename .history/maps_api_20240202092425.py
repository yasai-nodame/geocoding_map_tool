import folium
from folium import Circle
import main

def latitude_longitude(longitude_latitude_list):
    folium_map = folium.Map(location=[longitude_latitude_list[1], longitude_latitude_list[0]], zoom_start=15)
    
    #半径をメートルに変換(1km = 1000メートル)
    radius_meters = 10 * 1000

    # folium.Marker(location=[longitude_latitude_list[1], longitude_latitude_list[0]],radius=500).add_to(folium_map)
    
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

