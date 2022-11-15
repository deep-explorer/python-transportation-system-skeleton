import csv
import pandas as pd
from tempfile import NamedTemporaryFile
import shutil

from user_def import User
from customer_def import Customer


class Transportation_system():

    def __init__(self) -> None:
        pass

    # user add, remove, update

    def add_user(self, user: User):
        coulums = ["id", "firstname", "lastname", "street", "building_number", "zip_code",
                   "city", "country_code", "mobile_number", "email_address", "password"]
        check_list = []
        with open(User.csv_path, "r", encoding="utf-8") as input_stream:
            reader = csv.reader(input_stream)
            for row in reader:
                for id in row[0:1]:
                    check_list.append(id)
        if str(user.id) not in check_list:
            with open(User.csv_path, "a", encoding="utf-8") as output_stream:
                writer = csv.DictWriter(output_stream, fieldnames=coulums)
                # writer.writerow(user)
                writer.writerow({
                    "id": user.id,
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                    "street": user.street,
                    "building_number": user.building_number,
                    "zip_code": user.zip_code,
                    "city": user.city,
                    "country_code": user.country_code,
                    "mobile_number": user.mobile_number,
                    "email_address": user.email_address,
                    "password": user.password
                })
        else:
            print('That id is already exist')

    def remove_user(self, user_id: int):
        coulums = ["id", "firstname", "lastname", "street", "building_number", "zip_code",
                   "city", "country_code", "mobile_number", "email_address", "password"]
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(User.csv_path, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=coulums)
            writer = csv.DictWriter(tempfile, fieldnames=coulums)
            for row in reader:
                if row['id'] == str(user_id):
                    print('deleting row ', row['id'])
                else:
                    writer.writerow(row)

        shutil.move(tempfile.name, User.csv_path)

    def update_user(self, user: User):
        coulums = ["id", "firstname", "lastname", "street", "building_number", "zip_code",
                   "city", "country_code", "mobile_number", "email_address", "password"]
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(User.csv_path, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=coulums)
            writer = csv.DictWriter(tempfile, fieldnames=coulums)
            for row in reader:
                if row['id'] == str(user.id):
                    print('updating row ', row['id'])
                    row['firstname'], row['lastname'], row['street'], row['building_number'], row['zip_code'], row['city'], row['country_code'], row['mobile_number'], row['email_address'], row[
                        'password'] = user.firstname, user.lastname, user.street, user.building_number, user.zip_code, user.city, user.country_code, user.mobile_number, user.email_address, user.password
                writer.writerow(row)

        shutil.move(tempfile.name, User.csv_path)

    # customer add, remove, update

    def add_customer(self, customer: Customer):
        coulums = ["id", "company_name", "company_address_street", "company_address_building_number", "company_address_zip_code", "company_address_city",
                   "reference_person_firstname", "reference_person_lastname", "reference_person_country_code", "reference_person_number", "reference_person_email_address", "company_invocies_email_address"]
        check_list = []
        with open(Customer.csv_path, "r", encoding="utf-8") as input_stream:
            reader = csv.reader(input_stream)
            for row in reader:
                for id in row[0:1]:
                    check_list.append(id)
        if str(customer.id) not in check_list:
            with open(Customer.csv_path, "a", encoding="utf-8") as output_stream:
                writer = csv.DictWriter(output_stream, fieldnames=coulums)
                writer.writerow({
                    "id": customer.id,
                    "company_name": customer.company_name,
                    "company_address_street": customer.company_address_street,
                    "company_address_building_number": customer.company_address_building_number,
                    "company_address_zip_code": customer.company_address_zip_code,
                    "company_address_city": customer.company_address_city,
                    "reference_person_firstname": customer.reference_person_firstname,
                    "reference_person_lastname": customer.reference_person_lastname,
                    "reference_person_country_code": customer.reference_person_country_code,
                    "reference_person_number": customer.reference_person_number,
                    "reference_person_email_address": customer.reference_person_email_address,
                    "company_invocies_email_address": customer.company_invocies_email_address
                })
        else:
            print('That id is already exist')

    def remove_customer(self, customer_id: int):
        coulums = ["id", "company_name", "company_address_street", "company_address_building_number", "company_address_zip_code", "company_address_city",
                   "reference_person_firstname", "reference_person_lastname", "reference_person_country_code", "reference_person_number", "reference_person_email_address", "company_invocies_email_address"]
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(Customer.csv_path, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=coulums)
            writer = csv.DictWriter(tempfile, fieldnames=coulums)
            for row in reader:
                if row['id'] == str(customer_id):
                    print('deleting row ', row['id'])
                else:
                    writer.writerow(row)

        shutil.move(tempfile.name, Customer.csv_path)

    def update_customer(self, customer: Customer):
        coulums = ["id", "company_name", "company_address_street", "company_address_building_number", "company_address_zip_code", "company_address_city",
                   "reference_person_firstname", "reference_person_lastname", "reference_person_country_code", "reference_person_number", "reference_person_email_address", "company_invocies_email_address"]
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        with open(Customer.csv_path, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=coulums)
            writer = csv.DictWriter(tempfile, fieldnames=coulums)
            for row in reader:
                if row['id'] == str(customer.id):
                    print('updating row ', row['id'])
                    row["company_name"], row["company_address_street"], row["company_address_building_number"], row["company_address_zip_code"], row["company_address_city"], \
                        row["reference_person_firstname"], row["reference_person_lastname"], row["reference_person_country_code"], row["reference_person_number"], row["reference_person_email_address"], row["company_invocies_email_address"] \
                        = customer.company_name, customer.company_address_street, customer.company_address_building_number, customer.company_address_zip_code, customer.company_address_city, customer.reference_person_firstname, customer.reference_person_lastname, \
                        customer.reference_person_country_code, customer.reference_person_number, customer.reference_person_email_address, customer.company_invocies_email_address
                writer.writerow(row)

        shutil.move(tempfile.name, Customer.csv_path)
