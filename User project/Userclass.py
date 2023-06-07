from Utils import get_input
from contacts import *
import os
from abc import ABC, abstractclassmethod, abstractmethod
from validation import *
import pickle
import csv
import pathlib

class BaseModel(ABC):    
    def save_file(self):
        info_file=pathlib.Path(self.get_file_path())
        if info_file.exists():
            info=self.read_pickle()

            info.append(self.get_file_content())

            with open(self.get_file_path(),'wb') as f:
                pickle.dump(info,f)

        else:
            with open(self.get_file_path(), "wb") as f:
                pickle.dump([self.get_file_content()],f)

        
    @abstractmethod
    def get_file_path(self):
        pass

    @abstractmethod
    def get_file_content(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def from_str(cls, s: str):
        pass

    @abstractmethod
    def read_pickle(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_all_path(cls) -> list[str]:
        pass



class User(BaseModel):

    username = UserValid()
    password = PasswordValid()

    def __init__(self,username, password):
        self.username = username
        self.password = password

    @staticmethod
    def get_file_path():
        return "Users.pickle"
    
    @staticmethod
    def read_pickle():
        with open(User.get_file_path(),"rb") as f:
            return pickle.load(f)


    def get_file_content(self) -> str:
        return f"{self.username}||{self.password}"
    
    @classmethod
    def from_str(cls, s: str):
        username,password= s.split("||")
        return cls(username,password)

    @classmethod
    def get_all_path(cls) -> list[str]:
        return [path for path in os.listdir() if path.endswith("Users.pickle")]
    

    @classmethod
    def register(cls,username,password):
        return  cls(username,password)

    @classmethod
    def login(cls, username, password):
        check = pathlib.Path("Users.pickle")
        if check.exists():
            users = cls.read_pickle()
            for user in users:
                user = user.split("||")
                if user[0] == username and user[1] == password:
                    return  True
            else:
                print("User is not set")


#---------------------------------------------------------------------------



def add_contacts():
    print("Enter your contact details:")
    name=get_input("Name: ", target_type=str)
    email=get_input("Email: ", target_type=str)
    phone=get_input("Phone: ", target_type=str)

    contact= Contacts(name=name, email=email, phone=phone)
    contact.save_file()
    print("Contact is create successfully.\n")

def edit_contacts():
    contact_name=get_input("Enter the contact name: ", target_type=str)
    try:
        check =Contacts.find_by_id(contact_name)
    except:
        print("Contact was not found.\n")
        return
    check.delete()
    

    if check:
        name=get_input("Name: ", target_type=str)
        email=get_input("Email: ", target_type=str)
        phone=get_input("Phone: ", target_type=str)

        contact= Contacts(name=name, email=email, phone=phone)
        contact.save_file()
        print("Contact is edit successfully.\n")
    


def delete_contact():
    contact_name = get_input("Enter the contact name: ", target_type=str)
    try:
        print(" ")
        name = Contacts.find_by_id(contact_name)
        name.delete()
        print("\nYour contact was deleted.")
    except:
        print("Contact was not found")
        return
    
def search_nam():
    enter=get_input("Enter Name for searhing:\n")
    try:
        print(" ")
        check=Contacts.search_name(enter)
        print(check)
    except:
        print("Contact was not found")
        return
    
def search_mail():
    enter=get_input("Enter Email for searhing:\n")
    try:
        print(" ")
        check=Contacts.search_email(enter)
        print(check)
    except:
        print("Contact was not found")
        return
    
def search_phon():
    enter=get_input("Enter Phone number for searhing:\n")
    try:
        check=Contacts.search_phone(enter)
        print(check)
    except:
        print("Contact was not found")
        return


def view_all_contacts():
    info_file=pathlib.Path("contacts.pickle")
    if info_file.exists():
        for contact in Contacts.read_pickle():
            print(contact)
    else:
        print("File does not exist")
    

def csv_file():
    aggregate=[]
    for contact in Contacts.read_pickle():
        aggregate+=contact
        
    with open("contacts.csv", "w") as f:
        for line in aggregate:
            f.write(line.replace(",", ""))
        line=csv.writer(f)
    print("Your CSV file was created successfully!")


def page_exit():
    print("Good bye!")
    exit()
    
