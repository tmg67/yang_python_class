import numpy as np
#puzzel: find the sum of elements along the diagonal and flip the matrix
#Generate a random 4x4 matrix with values from 1 to 20
matrix = np.random.randint(1,21,(4,4))
print("Original Matrix:")
print(matrix)

#calculate the sum of the diagonal
diagonal_sum = np.trace(matrix)
print(f"\n sum of diagonal elements: {diagonal_sum}")

#Flip the matrix vertically and horizontally
flipped_matrix = np.flip(matrix)
print("\nFlipped Matrix:")
print(flipped_matrix)

#Bonus: identify positions of elements greater than 15
positions = np.argwhere(matrix > 15)
print("\nPositions of elements greater than 15:")
for pos in positions:
    print(f"Row {pos[0] +1 }, Column {pos[1]+1}")
    #csv comma separated values
    #tsv tab separated values
import csv

#File path for sales tracker
file_path = "sales_trackers.csv"

#create a new cvs file with headers
def create_csv():
    headers = ["date", "product", "quantity", "price per unit", "total"]
    with open(file_path, mode="w", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("sale tracker created.")

#add anew scale record to csv file
def add_sale(date, product, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, product, quantity, price_per_unit, total])
    print("sale record added")
#calculate total sales from the CSV file
def calculate_total_sales():
    total_sales  = 0
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["total"])
    print(f"toatal sales: ${total_sales:.2f}")

#example usage
create_csv()
add_sale("2025-01-06", "laptop", 2, 1200.50)
add_sale("2025-01-06", "mouse", 5, 25.99)
calculate_total_sales()
