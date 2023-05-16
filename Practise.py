cities = {"Machester":{"info":{"Size":"4m", "Region": "NW"}},
"London":{"info" :{"Size" : "9M ",
          "Region": "NW"}},
"Birmingham" : {"info":{"Size":"2M",
           "Region": "MD"}}}
for city in cities.keys():
    print(city)
    print(cities [city]["info"]["Size"])
    print(cities[city]["info"]["Region"])          
