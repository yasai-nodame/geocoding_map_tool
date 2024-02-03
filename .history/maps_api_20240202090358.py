import folium
import main

folium_map = folium.Map(location=[35.69389, 139.703613], zoom_start=15)

folium.Marker(location=[35.69389, 139.703613]).add_to(folium_map)

folium_map.save("map.html")