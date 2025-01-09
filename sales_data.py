import csv
import random
import numpy as np

#File path for sales tracker
sales_data_file = "sales_data.csv"
summary_data_file = "sales_summary.csv"

#create a new cvs file with headers
def create_csv():
    """creates a csv file with headrers"""
    headers = [ "product", "region", "sales", "price", "total"]
    with open(sales_data_file, mode="w", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def add_sale(product, region, sales, price):
    total = sales * price 
    with open(sales_data_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, region, sales, price,total])
    print("sale record added")
#generate random sales data and append to the csv
def generate_random_sales_data(num_records):
    products = ["laptop", "smartphone", "tablet", "headphone"]
    regions = ["pokhara", "kathmadu", "birgunj", "illam"]

    for _ in range(num_records):
        product = random.choice(products)
        region = random.choice(regions)
        sales = random.randint(10, 500)#random units sold
        price = round(random.uniform(10.0, 2000.0), 2)#random price
        add_sale(product, region, sales, price)
    print(f"generated {num_records} random sales records")

   
#analyze sales dtaa and write summaryt o a new file 
def analyze_sales_data():
    sales_data = []
    #read data from the sales CSV
    with open(sales_data_file, mode= "r")as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["sales"] = int(row["sales"])
            row["price"] = float(row["price"])
            row["revenue"] = row["sales"]*row["price"]
            sales_data.append(row)

    #calculate metrics using numpy
    revenues = np.array([row["revenue"] for row in sales_data])
    average_revenue = np.mean(revenues)
    product_revenue_map = {row["product"]: row["revenue"] for row in sales_data}
    product_with_highest_revenue = max(product_revenue_map, key = product_revenue_map.get)
    region_revenue_map = {}
    for row in sales_data:
        region = row["region"]
        region_revenue_map[region] = region_revenue_map.get(region, 0) + row["revenue"]

        #write summary to a new csv
        with open(summary_data_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["product", "total revenue", "region"])
            for row in sales_data:
                writer.writerow([row["product"], row['revenue'], row["region"]])
        #print summary results
        print("\n analysis summary:")
        print(f"average revenue: ${average_revenue:.2f}")
        print(f"""product with highest revenue:
        {product_with_highest_revenue} (${product_revenue_map[product_with_highest_revenue]:.2f})""")
        print("total revenue by region:")
        for region, revenue in region_revenue_map.items():
            print(f" - {region}; ${revenue:.2f}")
create_csv()
generate_random_sales_data(10)
analyze_sales_data()