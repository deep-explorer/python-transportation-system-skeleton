
class Customer():
    id_iterator = 1
    csv_path = 'database/customer.csv'

    def __init__(self, company_name, company_address_street, company_address_building_number, company_address_zip_code, company_address_city, reference_person_firstname, reference_person_lastname, reference_person_country_code, reference_person_number, reference_person_email_address, company_invocies_email_address):
        self.id = Customer.id_iterator
        Customer.id_iterator += 1

        self.company_name = company_name
        self.company_address_street = company_address_street
        self.company_address_building_number = company_address_building_number
        self.company_address_zip_code = company_address_zip_code
        self.company_address_city = company_address_city
        self.reference_person_firstname = reference_person_firstname
        self.reference_person_lastname = reference_person_lastname
        self.reference_person_country_code = reference_person_country_code
        self.reference_person_number = reference_person_number
        self.reference_person_email_address = reference_person_email_address
        self.company_invocies_email_address = company_invocies_email_address

    def set_company_name(self, company_name):
        self.company_name = company_name

    def set_reference_person_firstname(self, firstname):
        self.firstname = firstname
