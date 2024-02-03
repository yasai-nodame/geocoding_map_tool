from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import OpenCage

api_key = '1ed415b65ba44d98aa3c6f61861aeb83'
geolocator = OpenCage(api_key)

latitude = 35.69389
longitude = 139.703613

location = geolocator.reverse((latitude, longitude),language='ja')

if location:
    print(location.address)
else:
    print('ジオコーディングができませんでした')