from Utils import *
import re


class UserValid:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not valid_username(value):
            raise ValueError(
                    "Username must have 4 to 16 characters, one uppercase, one lowercase"
                )
            
        instance.__dict__[self.name] = value

def valid_username(value):
    patern = r"^[a-zA-Z\d]{4,16}$"
    checking = re.match(patern, value)
    return bool(checking)


#--------------------------------------------------------------

class PasswordValid:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not valid_password(value):
            raise ValueError(
                    "Password must have at least 8 characters, one uppercase, one lowercase, and one digit"
                )
            
        instance.__dict__[self.name] = value

def valid_password(value):
    patern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    checking = re.match(patern, value)
    return bool(checking)

#--------------------------------------------------------------

class EmailValid:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not email_check(value):
            raise ValueError(
                    "Email address is not valid"
                )
        
        instance.__dict__[self.name] = value

def email_check(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}\b'
    check=re.match(pat,email)
    return bool(check) 

#--------------------------------------------------------------


class PhoneValid:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not phone_check(value):
            raise ValueError(
                    "Phone number is not valid"
                )
            
        instance.__dict__[self.name] = value

def phone_check(number):
    pat=r"^(09(\d{9}))$"
    check=re.match(pat,number)
    return bool(check)

