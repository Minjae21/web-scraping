# BetterBasket Technical Assessment

This Python project scrapes the full list of products available at any Whole Foods Market store, using their internal API. The output is saved in a structured CSV filem containing product details - such as name, brand, price, and more.

---

## Features
- Input a Whole Foods store ID
- Fetch **all available products**, paginated in batches of 60
- Save the full products list in a CSV file with all attributes
- **Optional tool:** get `store_id` by simply typing a specific location(city) of the store:
```bash
python store_id.py
```
---
### Usage
1. Scrape all products by store ID
```bash
python app.py --store 10044
```
### Optional limit:
```bash
python app.py --store 10044 --max 120
```
### The CSV output file will be named:
wholefoods_products_10044.csv

---
### Install dependencies
If you plan to use the optional feature, you must run:
```bash
pip install -r requirements.txt
```
