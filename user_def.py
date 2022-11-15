
class User():
    id_iterator = 1
    csv_path = 'database/user.csv'

    def __init__(self, firstname, lastname, street, building_number, zip_code, city, country_code, mobile_number, email_address, password):
        self.id = User.id_iterator
        User.id_iterator += 1

        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.building_number = building_number
        self.zip_code = zip_code
        self.city = city
        self.country_code = country_code
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.password = password  # required to encrypt

    def get_fullname(self):
        return self.firstname + ' ' + self.lastname

    def get_address(self):
        return self.street + ' ' + str(self.building_number) + ' ' + str(self.zip_code) + ' ' + self.city

    def get_mobile_number(self):
        return '+' + str(self.country_code) + str(self.mobile_number)

    def set_firstname(self, firstname):
        self.firstname = firstname

    def to_string(self):
        return 'Full Name: ' + self.firstname + ' ' + self.lastname + '\n'
