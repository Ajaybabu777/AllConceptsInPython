import time

def chooseItem(item):
    print(f"picking {item} from the store")
    time.sleep(5)
    print(f"{item} picked")

def scan(item):
    print(f"scanning of {item} compmpleted")
    time.sleep(3)
    print(f'{item} scanned')

def checkout(items):
    for item in items:
        chooseItem(item)
        scan(item)
    print("checkout completed")


shopList = ["bedsheets", "pillow", "pilow cover","mattress"]
checkout(shopList)