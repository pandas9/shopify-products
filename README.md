# shopify-products

## Import products into your store from any store

Script that will convert shopify products.json into importable CSV file for shopify


## Run

`python convert.py`


## How it works

Example url https://compliancewarehouse.com/products.json?limit=250&page=1 that will download products.json which is equal to products_example.json inside project folder

import_example.csv is shopify import example that shopify provides

products_generated_example.csv is output after you run script

If you set `Variant Inventory Policy` to `continue` it will allow people to purchase product when quantity is 0 if policy is `deny` its the opposite


## Requirements

python>=3
