import random
import string
from ROT13 import ROT13


class UserProfile:

    # Data/Information
    def __init__(self):
        self.__username = None
        self.__password = ""
        self.__salary = None
        self.id = self.__generate_id()
        self.__job_title = ""
        self.clearance = 0

    # private method, __ before function name makes it private
    def __generate_id(self):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # class method
    @staticmethod
    def class_method():
        print("I am a class method")

    def get_username(self):
        return self.__username

    def set_username(self, username):
        if len(username) < 4 or len(username) > 20:
            raise Exception("Username must be between 4 an 20 characters")
        else:
            self.__username = username

    def set_password(self, current_password, new_password):
        if self.hash_password(current_password) != self.__password:
            return
        else:
            self.__password = self.hash_password(new_password)

    # hash_password - encrypt password to be stored

    def hash_password(self, string):
        # possibly use rot13
        return ROT13.encrypt(string)

    # login - displays profile information
    def login(self, username, password):
        if username == self.__username and self.hash_password(password) == self.__password:
            print(f"Username: {self.__username}")
            print(f"ID: {self.id}")
            print(f"Salary: {self.__salary}")
            print(f"Job Title: {self.__job_title}")
            print(f"Clearance: {self.clearance}")
        else:
            raise Exception("Invalid username or password...")

    # pay_raise - increase salary based on given percentage

    def pay_raise(self, profile, percentage):
        if self.check_clearance() == True:
            new_pay = profile.__salary * percentage
            profile.__salary += new_pay
        else:
            print("You do not have sufficient credentials...")

    def get_salary(self):
        return self.__salary

    def set_salary(self, profile, salary):
        if self.check_clearance() == True:
            profile.__salary = salary
        else:
            print("You do not have sufficient credentials...")

    def set_job_title(self, profile, job_title):
        if self.check_clearance() == True:
            profile.__job_title = job_title
        else:
            print("You do not have sufficient credentials...")

    # check_clearance - return true/false
    def check_clearance(self):
        return self.clearance > 3

    def load_profile(self, dict):
        self.__username = dict['username']
        self.__password = dict['password']
        self.id = dict['id']
        self.__salary = dict['salary']
        self.__job_title = dict['job_title']
        self.clearance = dict['clearance']

        return self

import json
def read_file():
    with open('./profiles.json') as file:
        # file.read returns a string
        contents = file.read()

    # json.loads converts jsonstring into python datatypes
    profiles = json.loads(contents)
    return profiles



def main():
    people = read_file()
    employees = []
    
    for person in people:
        employee = UserProfile().load_profile(person)
        employees.append(employee)

main()