# main technical assessment file
import argparse
import requests
import csv

def get_products(store_id, max_limit=None):
    offset = 0
    limit = 60
    total_products = []

    url = "https://www.wholefoodsmarket.com/api/products/category/all-products"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    while True:
        params = {
            "leafCategory": "all-products",
            "store": store_id,
            "limit": limit,
            "offset": offset
        }

        try:
            r = requests.get(url, headers=headers, params=params)
            r.raise_for_status()
            data = r.json()

        except Exception as e:
            print(f"Error: {e}")
            break

        products = data.get("results", [])

        if not products:
            print("No more products found - the end.")
            break

        print(f"Got {len(products)} products - current offset {offset}.")
        total_products.extend(products)
        offset += limit

        if max_limit is not None and len(total_products) >= max_limit:
            total_products = total_products[:max_limit]
            print(f"Finished getting max limit of {max_limit} products.")
            break

    return total_products

def save_csv(products, filename):
    if not products:
        print("No products to save.")
        return

    csv_cols = products[0].keys()

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=csv_cols)
        writer.writeheader()

        for p in products:
            row = {key: p.get(key, 'N/A') for key in csv_cols}
            writer.writerow(row)

    print(f"Saved {len(products)} products to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Scraping all products at Whole Foods.")
    parser.add_argument("--store", required=True, type=int, help="Store ID (For example: 10044)")
    parser.add_argument("--max", type=int, default=None, help="(Optional) max number of products to fetch")
    args = parser.parse_args()

    store_id = args.store

    print(f"Scraping products for store ID: {store_id}...")
    products = get_products(store_id, max_limit=args.max)

    if products:
        csv_filename = f"wholefoods_products_{store_id}.csv"
        save_csv(products, csv_filename)
    else:
        print("No products found.")

if __name__ == "__main__":
    main()
