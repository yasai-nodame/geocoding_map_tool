from opencage.geocoder import OpenCageGeocode

OCG = OpenCageGeocode('1ed415b65ba44d98aa3c6f61861aeb83')
results = OCG.reverse_geocode(35.69389,139.703613)
print(results)