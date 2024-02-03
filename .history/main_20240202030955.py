import requests 

def search_osm_places(latitude, longitude, radius, amenity):
    overpass_url = "https://lz4.overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    node(around:{radius},{latitude},{longitude})["amenity"="{amenity}"]
    out body;
    """
    
    response = requests.post(overpass_url,data=query)
    data = response.json()
    return data 

results = search_osm_places(40.7128, -74.006, 1000, "restaurant")
print(results)