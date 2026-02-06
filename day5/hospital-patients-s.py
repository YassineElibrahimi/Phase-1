# Deliverable:
# Python script that stores patient records, tracks unique medical conditions, and enables condition-based search.

import random


def menu():
    print("-" * 40)
    print("======= Hospital-Patients-System =======")
    print("-" * 40)
    print("1. Add patient")
    print("2. Display patients records")
    print("3. See the conditions we have")
    print("4. Search by condition")
    print("5. Exit")


def generate_id():
    patient_id = random.randint(0, 9999)
    patient_id = f"{patient_id:04d}"
    return patient_id


def add_patient(patient_id, name, age, condition):
    new_patient = {f"ID_{patient_id}": {"name": name, "age": age, "condition": condition}}
    return new_patient





def main():
    record_sys = {}
    conditions = set()

    while True:
        menu()
        user = int(input("\nChoose an Operation: "))

        # ___________________ Add new patients ___________________
        if user == 1:
            patient_id = generate_id()
            name = input("Enter patients name")
            age = input("Enter patients age")
            condition = input("Enter patients condition")
            record_sys.update(add_patient(patient_id, name, age, condition))
            conditions.add(condition)
            print("Patient is added successfully\n")


        # ___________________ Display all records ___________________
        elif user == 2:
            if not record_sys:
                print("The record system is Empty")
            else:
                for patient_id, patient_data in record_sys.items():
                    print(patient_data)


        # ___________________ Display all conditions ___________________
        elif user == 3:
            if not conditions:
                print("The conditions record is Empty")
            else:
                for condition in conditions:
                    print(condition)

        # ___________________ Search by condition ___________________
        elif user == 4:
            search_by_condition = input("Enter a condition: ")
            found = False
            for patient_id, patient_data in record_sys.items():
                if patient_data["condition"] == search_by_condition:
                    print(f"Patient: {patient_id} - {patient_data}")
                    found = True
            if not found:
                print("No patients with that condition")
        if user == 5:
            print("Program Exit")
            break
main()