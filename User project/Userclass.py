from contacts import *
import os
from abc import ABC, abstractclassmethod, abstractmethod
from validation import *
import pickle
import pathlib
from base import *



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




