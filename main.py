import requests
import json


def main(item):
    itemparts = item.split()
    capitemparts = [i.capitalize() for i in itemparts]
    item = " ".join(capitemparts)

    allitems = []

    ah = json.loads(requests.get(f"https://api.hypixel.net/skyblock/auctions").text)
    for j in range(ah["totalPages"]):
        ah = json.loads(requests.get(f"https://api.hypixel.net/skyblock/auctions?page={j}").text)
        for i in ah["auctions"]:
            if item in i["item_name"]:
                if i["bin"]:
                    allitems.append(i)

    allitems = sorted(allitems, key=lambda x: x[sortby])
    allitems = json.dumps(allitems, indent=4)
    return allitems


if __name__ == "__main__":
    item = input("Item: ")
    sortby = input("Sort by (starting_bid/end): ")
    lowestbin = main(item)
    print(lowestbin)
