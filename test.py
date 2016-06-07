import requests;


cookie = {'steamLogin': '76561198071419140%7C%7C490C5409FEBCAA2D4CF88E53B08527AA08A18FBE'};
r = requests.get("http://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name=AK-47%20%7C%20Frontside%20Misty%20%28Field-Tested%29", cookies=cookie);
#data = r.json();
print(r.text);