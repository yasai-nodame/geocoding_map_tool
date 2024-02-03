import folium
import main

def latitude_longitude(longitude_latitude_list[]):
    folium_map = folium.Map(location=[longitude_latitude_list[1], longitude_latitude_list[0]], zoom_start=15)

    folium.Marker(location=[35.69389, 139.703613]).add_to(folium_map)

    folium_map.save("map.html")

latitude_longitude(main.latitude_longitude())

