# Customer class
class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name

    def set_address(self, address):
        self.__address

    def set_phone(self, phone):
        self.__phone

    def get_name(self):
        return self.__name

    def get_address(self, address):
        return self.__address

    def get_phone(self):
        return self.__phone