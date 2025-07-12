# This file is optional: helper to get the store id based on the location
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_store_id(store_url):
    response = requests.get(store_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    selector = soup.find("wfm-store-selector")
    if selector and selector.has_attr("store-id"):
        return selector["store-id"]

    return None

def main():
    slug = input("Enter store location without any space (For example: Franklin, Westloop): ").strip()
    store_url = f"https://www.wholefoodsmarket.com/stores/{slug}"
    store_id = get_store_id(store_url)
    if store_id:
        print(f"Store ID for {slug}: {store_id}")
    else:
        print("No store_id available from that location.")

if __name__ == "__main__":
    main()
