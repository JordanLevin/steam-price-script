import requests;

r = requests.get("http://api.csgo.steamlytics.xyz/v1/items?key=abaded45347a777a0b11eb028072c7ec");
data = r.json();
file = open("ItemList.txt","w",encoding='utf-8');
for i in data['items']:
    file.write(i['market_hash_name']+"\n");
file.close();
#print(data['items'].keys());
#print(data);
#print (data['market_hash_name']);
