import csv
import openpyxl
import numpy as np
import random


student_score_file = "student_scores.csv"
file_path = "results.xlsx"
def create_csv():
    """creates a csv file with headers"""
    headers = [ "name", "subject","score"]
    with open(student_score_file, mode="w", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(headers)
def add_score(name,subject,score): 
    with open(student_score_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, subject, score])
    print("score record added")

def generate_random_students_data(num_records):
    name = ["alice","bob","alice","bob","charlie","charlie"]
    subject = ["maths", "math","science", "science","math", "science"]
    score = [85, 90, 95, 80, 70, 75 ]


    for _ in range(num_records):
        names = random.choice(name)
        subjects = random.choice(subject)
        scores = random.randint(10, 100)


        add_score(name, subject, score )
    print(f"generated {num_records} random score records")
def analyze_score_data():
    score_data = []
    #read data from the sales CSV
    with open(student_score_file,mode= "r")as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["name"] = row["name"]
            row["subject"] = row["subject"]
            row["score"] = int(row["score"])
            score_data.append(row)

create_csv()
generate_random_students_data(10)
analyze_score_data()