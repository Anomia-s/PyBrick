import requests  # Import requests


class UserFunctions:
    def GatherFullInfo(userId):
        url = 'https://api.brick-hill.com/v1/user/profile?id='+str(userId)
        resp = requests.get(url=url)
        data = resp.json()
        print("Brick Hill Info Gathering System\nUsername: "+data["username"] + "\nLast Seen: " +data["last_online"]+"\nAccount Created at the date of "+data["created_at"]+"\nStatus: "+ data["status"][0]["body"]) 
    def GatherInfo(userId, Filter):
        url = 'https://api.brick-hill.com/v1/user/profile?id='+str(userId)
        resp = requests.get(url=url)
        data = resp.json()
        if Filter == "username" or "Username":
            return data["username"]
        if Filter == "description" or "blurb" or "Description":
            return data["description"]
        if Filter =="last_online" or "Last Online" or "Last online" or "last online":
            return data["last_online"]
        
    def ToId(username):
        url = 'https://api.brick-hill.com/v1/user/id?username=' + username
        resp = requests.get(url=url)
        data = resp.json()
        return data["id"]


class ShopFunctions:
    def GetItemInfo(ItemID, Filter):
        url = "https://api.brick-hill.com/v1/shop/item?id="+ItemID
        resp = requests.get(url=url)
        data = resp.json()
        if Filter == "name":
            return data[0]["name"]
        if Filter == "bits":
            if data[0]["bits"] == -1:  #data[0] returns raw data instead of Json one.
                return "Not for sale with bits."
            else:
                return data[0]["bits"]
        if Filter == "bucks":
            return data["bucks"]
        if Filter == "id":
            return data[0]["id"]
        if Filter == "sold_out" or "sold out":
            if data[0]["sold_out"] == True:
                print("Item is sold out")
            else:
                print("Item is not sold out")
        
        
    def GetLatestItem(ItemType, DetailType):
        url = "https://www.brick-hill.com/api/shop/main/" +  ItemType + "/updated/1/?page_size=1&bot_friendly"
        resp = requests.get(url=url)
        data = resp.json()
        # AHAHAH
        if DetailType == "name":
            return data[0]["name"]
        if DetailType == "bits":
            if data[0]["bits"] == -1:  #data[0] returns raw data instead of Json one.
                return "Not for sale with bits."
            else:
                return data[0]["bits"]
        if DetailType == "bucks":
            return data[0]["bucks"]
        if DetailType == "id":
            return data[0]["id"]
        if DetailType == "sold_out" or "sold out":
            if data[0]["sold_out"] == True:
                print("Item is sold out")
            else:
                print("Item is not sold out")

# TypeError: list indices must be integers or slices, not str Fixed
class ClanFunctions:
    def GetClanInfo(ClanId, Filter):
        RealID = str(ClanId)
        url = 'https://api.brick-hill.com/v1/clan/clan?id=' + RealID
        resp = requests.get(url=url)
        data = resp.json()
        if Filter == "name":
            return data[0]["name"]
        if Filter == "id":
            return data[0]["id"]
        if Filter == "tag":
            return data[0]["tag"]
        if Filter == "title":
            return data["title"]
        if Filter == "all":
            return data["title"],data["tag"],data["id"]










        #<a
