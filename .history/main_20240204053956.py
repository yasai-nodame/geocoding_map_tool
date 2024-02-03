import requests
import urllib 
import restaurant_search

latitude_longitude_list = []
def latitude_longitude():
    makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

    #今回は特定の3社のホームページの情報を取得するため、その会社の住所を入力
    input_address = input('検索したい住所を入力してください')
    s_quote = urllib.parse.quote(input_address)
    response = requests.get(makeUrl + s_quote)
    latitude_longitude_list = response.json()[0]['geometry']['coordinates']
    print(latitude_longitude_list)
    # return latitude_longitude_list
    
latitude_longitude()

# restaurant_search.restaurant_to_dataframe(latitude=coordinates[1],longitude=coordinates[0])