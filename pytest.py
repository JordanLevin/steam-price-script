import requests;
import time;

class Item(): #class for getting the price of an item
    def __init__(self, url):
        self.url = url;
        self.r = requests.get(url);
        self.price = 0;
        self.pprice = 0;
        self.ppprice = 0;
    def getPrice(self): #method that gets item price and returns it as a float
        content = self.r.content.decode("utf-8");
        if "median_price" in content:
            data = content.split(":");
            temp = data[len(data)-1];
            temp = temp.replace("\"","");
            temp = temp.replace("\\","");
            temp = temp.replace("u20ac","");
            temp = temp.replace("}","");
            temp = temp.replace(",","."); #replace some crap to format it correctly
            temp = temp.replace("-","0");
            self.price = float(temp);
            self.ppprice = self.pprice;
            self.pprice = self.price;
            return self.price;
        else:
            return 0;
    def getAvg(self): #return average price of the last 3 checks
        if self.pprice==0 or self.ppprice==0: #if the program just started just use current price
            return self.price;
        return (self.pprice+self.ppprice)/2
    def getUrl(self): #return the item url
        return self.url;



urlList = [];
itemList = [];
#do some stuff here to import list of items into urlList\
file = open("ItemList.txt","r",encoding='utf-8');
tempList = file.read().split("\n");
for i in range(len(tempList)):
    urlList.append("http://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name="+tempList[i]);
for i in range(len(urlList)):
    itemList.append(Item(urlList[i]));
file.close();
#itemTest = Item("http://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name="+); #just for testing
#itemList.append(itemTest);
output = open("Output.txt","w",encoding='utf-8');
while 1==1:

    for i in itemList:
        time.sleep(5);
        tempPrice = i.getPrice();
        tempAvg = i.getAvg();
        print(tempPrice, end = "   "); #temporary for testing
        print(i.getUrl());
        if tempPrice>tempAvg*3 and tempPrice >0 and tempAvg>0:
            print(i.getUrl()); #add item to the txt later
            output.write(i.getUrl());


    #time.sleep(10000) #add this later
