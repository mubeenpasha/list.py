import requests 


url = "https://api.github.com/search/repositories?q=labhuage:python&sort=stars"
req= requests.get(url)


print(req.status_code)
data = req.json()
data_dict = data.items()
#print(data.keys())
print (data["total count"] )
print(data["items"])
