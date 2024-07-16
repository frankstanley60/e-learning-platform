# import_csv.py

import csv
from .models import StudentResponse, Student

def import_csv_data(c:\Users\frank\Downloads\params3PL.csv, StudentResponse):
    with open(c:\Users\frank\Downloads\params3PL.csv, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            model_class.objects.create(**row)
