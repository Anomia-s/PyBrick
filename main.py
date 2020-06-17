import requests
class UserFunctions:
  def GetDescription(userId): 
    url = 'https://api.brick-hill.com/v1/user/profile?id='+userId
    resp = requests.get(url=url)
    data = resp.json() 
    return data["description"]

  def GetUsername(userId): 
    url = 'https://api.brick-hill.com/v1/user/profile?id='+userId
    resp = requests.get(url=url)
    data = resp.json() 
    return data["username"]
  def ToId(username):
    url = 'https://api.brick-hill.com/v1/user/id?username=' +username
    resp = requests.get(url=url)
    data = resp.json() 
    return data["id"]

class ShopFunctions:
  def GetLatestItem(ItemType, DetailType):
    url = "https://www.brick-hill.com/api/shop/main/" + ItemType + "/updated/1/?page_size=1&bot_friendly"
    resp = requests.get(url=url)
    data = resp.json() 
    print(data["description"])
    if DetailType=="name":
      return data["name"]
    if DetailType=="bits":
      return data["bits"]
    if DetailType == "bucks":
      return data["bucks"]
    if DetailType==""
  

