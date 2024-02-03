import requests
import urllib 
import restaurant_search

latitude_longitude_list = []
def latitude_longitude():
    makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

    #検索した住所の緯度・経度を取得
    input_address = input('検索したい住所を入力してください')
    s_quote = urllib.parse.quote(input_address)
    response = requests.get(makeUrl + s_quote)
    latitude_longitude_list = response.json()[0]['geometry']['coordinates']
    print(latitude_longitude_list)
    return latitude_longitude_list
    
latitude_longitude()

