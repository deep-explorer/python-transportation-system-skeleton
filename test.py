from transportation_system_def import Transportation_system
from user_def import User
from customer_def import Customer

service = Transportation_system()

# 1. add, remove, update for user
user1 = User(firstname='William', lastname='Lee', street='Street 1', building_number=123, zip_code=12, city='City 1',
             country_code=1, mobile_number=123456789, email_address='abc@example.com', password='Password@123')
user2 = User(firstname='Paul', lastname='Lee', street='Street 1', building_number=123, zip_code=12, city='City 1',
             country_code=1, mobile_number=123456789, email_address='abc@example.com', password='Password@123')

print(user1.to_string())

service.add_user(user1)
service.add_user(user2)
service.remove_user(user1.id)
user2.set_firstname('Kevin')
service.update_user(user2)

# 2. add, remove, update for corporate customer
customer1 = Customer(company_name='Company 1', company_address_street='Street 1', company_address_building_number=123, company_address_zip_code=111, company_address_city='City 1', reference_person_firstname='William',
                     reference_person_lastname='Lee', reference_person_country_code=1, reference_person_number=123456789, reference_person_email_address='reference@example.com', company_invocies_email_address='invoce@example.com')
customer2 = Customer(company_name='Company 2', company_address_street='Street 2', company_address_building_number=123, company_address_zip_code=111, company_address_city='City 1', reference_person_firstname='William',
                     reference_person_lastname='Lee', reference_person_country_code=1, reference_person_number=123456789, reference_person_email_address='reference@example.com', company_invocies_email_address='invoce@example.com')

service.add_customer(customer1)
service.add_customer(customer2)
service.remove_customer(customer1.id)
customer2.set_company_name('Updated Company 2')
service.update_customer(customer2)

# 3. add, remove, update for private customer
# private customer doesn't have company information
customer1 = Customer(company_name='', company_address_street='', company_address_building_number=-1, company_address_zip_code=-1, company_address_city='', reference_person_firstname='William',
                     reference_person_lastname='Lee', reference_person_country_code=1, reference_person_number=123456789, reference_person_email_address='reference@example.com', company_invocies_email_address='')
customer2 = Customer(company_name='', company_address_street='', company_address_building_number=-1, company_address_zip_code=-1, company_address_city='', reference_person_firstname='Paul',
                     reference_person_lastname='Molotov', reference_person_country_code=1, reference_person_number=123456789, reference_person_email_address='reference@example.com', company_invocies_email_address='')

service.add_customer(customer1)
service.add_customer(customer2)
service.remove_customer(customer1.id)
customer2.set_reference_person_firstname('Roy')
service.update_customer(customer2)
