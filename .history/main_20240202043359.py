import requests
import urllib 

makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="

input_address = input('検索したい住所を入力してください')
s_quote = urllib.parse.quote(input_address)
response = requests.get(makeUrl + s_quote)
print(response.json()[0]['geometry']['coordinates'])