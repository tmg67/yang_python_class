import csv

def parse_csv_for_totals(file_path):
    #initialize  containers for row and  column totals
    row_totals = {}
    column_totals = {}

    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)#read the header row
        #initialize colum totals dictionary with column names
        for header in headers[1:]:#skips the first column(category)
            column_totals[headers] = 0

            #process rows
        for row in reader:
            category = row[0]#first column in category
            values =  list(map(int, row[1:]))# convert the rest of the row
            #values = [ 10,20,30]
            #calculate row total
            row_totals[category] = sum(values)
            #{
            # "A": 60
            #}
            #update colulmn totals
            for header, value in zip(headers[1:], values):
                column_totals[header] += value

    #output results
    print("row totals:")
    for category, total in row_totals.items():
        print(f"{category}: {total}")

    print("\ncolumn totals:")
    for column, total in column_totals.items():
        print(f"{column}: {total}")

#example usage
file_path = "parser_data.csv"
parse_csv_for_totals(file_path)


