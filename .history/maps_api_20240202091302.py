import folium
import main

def latitude_longitude(longitude,latitude):
    folium_map = folium.Map(location=[latitude, longitude], zoom_start=15)

    folium.Marker(location=[35.69389, 139.703613]).add_to(folium_map)

    folium_map.save("map.html")

get_latitude_longitude = latitude_longitude

print(type(get_latitude_longitude[0]))