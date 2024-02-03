import requests

def download_osm_data(bbox):
    overpass_url = "https://lz4.overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
        way({bbox});
        >;
    );
    out body;
    """
    response = requests.post(overpass_url, data=query)
    data = response.json()
    return data

# Example: Download OSM data for a bounding box (e.g., Tokyo)
bbox_tokyo = "35.5,139.5,35.9,140.0"
osm_data = download_osm_data(bbox_tokyo)
print(osm_data)