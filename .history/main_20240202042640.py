import requests
import urllib 

makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

input_address = input('検索したい住所を入力してください')
response = requests.get(makeUrl + input_address)
print(response.json())