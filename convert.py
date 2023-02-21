import json

import csv

fields = [
    'Handle',
    'Title',
    'Body (HTML)',
    'Vendor',
    'Product Category',
    'Type',
    'Tags',
    'Published',
    'Option1 Name',
    'Option1 Value',
    'Option2 Name',
    'Option2 Value',
    'Option3 Name',
    'Option3 Value',
    'Variant SKU',
    'Variant Grams',
    'Variant Inventory Tracker',
    'Variant Inventory Qty',
    'Variant Inventory Policy',
    'Variant Fulfillment Service',
    'Variant Price',
    'Variant Compare At Price',
    'Variant Requires Shipping',
    'Variant Taxable',
    'Variant Barcode',
    'Image Src',
    'Image Position',
    'Image Alt Text',
    'Gift Card',
    'SEO Title',
    'SEO Description',
    'Google Shopping / Google Product Category',
    'Google Shopping / Gender',
    'Google Shopping / Age Group',
    'Google Shopping / MPN',
    'Google Shopping / AdWords Grouping',
    'Google Shopping / AdWords Labels',
    'Google Shopping / Condition',
    'Google Shopping / Custom Product',
    'Google Shopping / Custom Label 0',
    'Google Shopping / Custom Label 1',
    'Google Shopping / Custom Label 2',
    'Google Shopping / Custom Label 3',
    'Google Shopping / Custom Label 4',
    'Variant Image',
    'Variant Weight Unit',
    'Variant Tax Code',
    'Cost per item',
    'Price / International',
    'Compare At Price / International',
    'Status'
]

rows = []

# Set to true if you are running first time and testing
test = False

with open('./products_example.json') as f:
    data = json.load(f)

    for product in data['products']:
        row = []
        row.append(product['handle']) # Handle
        row.append(product['title']) # Title
        row.append(product['body_html']) # Body (HTML)
        row.append('YOUR STORE NAME') # Vendor
        row.append('LEGAL SELLING CATEGORY') # Product Category https://help.shopify.com/txt/product_taxonomy/en.txt
        row.append(product['product_type']) # Type
        tags = ''
        for tag in product['tags']:
            tags += tag + ' '
        row.append(tags)
        row.append('TRUE')
        row.append('State') # Option1 Name

        # The way import csv is setup is that the first variant is the main variant
        # and the rest are sub variants. So we need to add the first variant and then
        # add the rest as sub variants
        # thats why we check if ind == 0 to add it to main row array as product
        for ind, variant in enumerate(product['variants']):
            if ind == 0:
                row.append(variant['option1'])
                row.append('') #option2
                row.append('') #option2
                row.append('') #option3
                row.append('') #option3
                row.append('') #sku
                row.append(variant['grams'])
                row.append('shopify') # Variant Inventory Tracker
                row.append('0') # Variant Inventory Qty
                row.append('continue') # Variant Inventory Policy
                row.append('manual') # Variant Fulfillment Service
                row.append(variant['price']) # Variant Price
                row.append(variant['compare_at_price']) # Variant Compare At Price
                row.append('TRUE') # Variant Requires Shipping
                row.append('TRUE') # Variant Taxable
                row.append('') # Variant Barcode
                row.append(product['images'][0]['src']) # Image Src
                row.append('1') # Image Position
                row.append('') # Image Alt Text
                row.append('FALSE') # Gift Card
                row.append('') # SEO Title
                row.append('') # SEO Description
                row.append('') # Google Shopping / Google Product Category
                row.append('') # Google Shopping / Gender
                row.append('') # Google Shopping / Age Group
                row.append('') # Google Shopping / MPN
                row.append('') # Google Shopping / AdWords Grouping
                row.append('') # Google Shopping / AdWords Labels
                row.append('') # Google Shopping / Condition
                row.append('') # Google Shopping / Custom Product
                row.append('') # Google Shopping / Custom Label 0
                row.append('') # Google Shopping / Custom Label 1
                row.append('') # Google Shopping / Custom Label 2
                row.append('') # Google Shopping / Custom Label 3
                row.append('') # Google Shopping / Custom Label 4
                row.append('') # Variant Image
                row.append('g') # Variant Weight Unit
                row.append('') # Variant Tax Code
                row.append('') # Cost per item
                row.append('') # Price / International
                row.append('') # Compare At Price / International
                row.append('active') # Status

                rows.append(row)
            else:
                variant_row = []

                variant_row.append(product['handle'])
                variant_row.append('') # Title
                variant_row.append('') # Body (HTML)
                variant_row.append('') # Vendor
                variant_row.append('') # Product Category
                variant_row.append('') # Type
                variant_row.append('') # Tags
                variant_row.append('') # Published
                variant_row.append('') # Option1 Name
                variant_row.append(variant['option1'])
                variant_row.append('') #option2
                variant_row.append('') #option2
                variant_row.append('') #option3
                variant_row.append('') #option3
                variant_row.append('') #sku
                variant_row.append(variant['grams'])
                variant_row.append('shopify') # Variant Inventory Tracker
                variant_row.append('0') # Variant Inventory Qty
                variant_row.append('continue') # Variant Inventory Policy
                variant_row.append('manual') # Variant Fulfillment Service
                variant_row.append(variant['price']) # Variant Price
                variant_row.append(variant['compare_at_price']) # Variant Compare At Price
                variant_row.append('TRUE') # Variant Requires Shipping
                variant_row.append('TRUE') # Variant Taxable
                variant_row.append('') # Variant Barcode
                variant_row.append('') # Image Src
                variant_row.append('') # Image Position
                variant_row.append('') # Image Alt Text
                variant_row.append('FALSE') # Gift Card
                variant_row.append('') # SEO Title
                variant_row.append('') # SEO Description
                variant_row.append('') # Google Shopping / Google Product Category
                variant_row.append('') # Google Shopping / Gender
                variant_row.append('') # Google Shopping / Age Group
                variant_row.append('') # Google Shopping / MPN
                variant_row.append('') # Google Shopping / AdWords Grouping
                variant_row.append('') # Google Shopping / AdWords Labels
                variant_row.append('') # Google Shopping / Condition
                variant_row.append('') # Google Shopping / Custom Product
                variant_row.append('') # Google Shopping / Custom Label 0
                variant_row.append('') # Google Shopping / Custom Label 1
                variant_row.append('') # Google Shopping / Custom Label 2
                variant_row.append('') # Google Shopping / Custom Label 3
                variant_row.append('') # Google Shopping / Custom Label 4
                variant_row.append('') # Variant Image
                variant_row.append('g') # Variant Weight Unit
                variant_row.append('') # Variant Tax Code
                variant_row.append('') # Cost per item
                variant_row.append('') # Price / International
                variant_row.append('') # Compare At Price / International
                variant_row.append('') # Status

                rows.append(variant_row)

                if test:
                    break
        if test:
            break

filename = "products_generated_example.csv"
# writing to csv file
with open(filename, 'w', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # writing the fields 
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)
