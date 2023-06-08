import os
from abc import ABC, abstractclassmethod, abstractmethod
from validation import *
import pathlib
from validation import *
import csv
import pickle
from base import *


class Contacts(BaseModel):
    name: str
    email=EmailValid()
    phone=PhoneValid()
    

    def __init__(self, name, email, phone,note=None,category=None) -> None:
        self.name=name
        self.email=email
        self.phone=phone
        self.note=note
        self.category=category

    @staticmethod
    def get_file_path():
        return "contacts.pickle" #for csv contacts.csv
    
    @staticmethod
    def read_pickle():
        with open(Contacts.get_file_path(),"rb") as f:
            return pickle.load(f)
    
    # @staticmethod
    # def read_csv():
    #     with open(Contacts.get_file_path(),"r") as f:
    #         a=csv.reader(f)
    #         lines=[]
    #         for line in a:
    #             lines+=line
    #         return lines

    def get_file_content(self) -> str:
        return f"{self.name}||{self.email}||{self.phone}||{self.note}||{self.category}"

    @classmethod
    def from_str(cls, s: str):
        name, email, phone= s.split("||")
        return cls(name, email, phone)

    @classmethod
    def get_all_path(cls) -> list[str]:
        return [path for path in os.listdir() if path.endswith("contacts.pickle")] #contacts.csv

    @classmethod
    def find_by_id(cls, name):
        # for e in cls.read_csv():
        for e in cls.read_pickle():
            x=e.split("||")[0]
            y=e.split("||")[1]
            u=e.split("||")[2]
            if x == name:
                return Contacts(x, y, u)
        assert None, "Not found"  # AssertionError

    def __repr__(self) -> str:
        return f"<contact #{self.name}>"

    def __str__(self):
        return f"Name: {self.name} - Email: {self.email} - Phone: {self.phone} - Note: {self.note} - Category: {self.category}"
    
    def delete(self):
        travelList = []
        L = self.read_pickle()
        
        for contact in L:
            contact1=contact.split('||')
            if(contact1[0] != self.name):
                travelList.append(contact)
        with open(self.get_file_path(), "wb") as f:
            pickle.dump(travelList,f)

        # with open(self.get_file_path(),'w') as f:
        #     for line in travelList:
        #         f.write(line.replace(",", ""))
        #     line=csv.writer(f)
        
    @classmethod
    def search_name(cls, name):
        # for e in cls.read_csv():
        for e in cls.read_pickle():
            x=e.split("||")[0]
            y=e.split("||")[1]
            u=e.split("||")[2]
            if x == name:
                return Contacts(x, y, u)
        assert None, "Not found"  # AssertionError
            

    @classmethod
    def search_email(cls,email):
        # for e in cls.read_csv():
        for e in cls.read_pickle():
            x=e.split("||")[0]
            y=e.split("||")[1]
            u=e.split("||")[2]
            if y == email:
                return Contacts(x, y, u)
        assert None, "Not found"  # AssertionError

    @classmethod
    def search_phone(cls,phone):
        # for e in cls.read_csv():
        for e in cls.read_pickle():
            x=e.split("||")[0]
            y=e.split("||")[1]
            u=e.split("||")[2]
            if u == phone:
                return Contacts(x, y, u)
        assert None, "Not found"  # AssertionError
    
    @classmethod
    def search_category(cls,category):
        # for e in cls.read_csv():
        for e in cls.read_pickle():
            x=e.split("||")[0]
            y=e.split("||")[1]
            u=e.split("||")[2]
            w=e.split("||")[3]
            k=e.split("||")[4]
            if k == category:
                print(Contacts(x,y,u,w,k))
            
        assert None, "Not found"  # AssertionError


#<------------------------------------------------------------------>



    