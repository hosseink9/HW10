from contacts import *


def add_contacts():
    print("Enter your contact details:")
    name=get_input("Name: ", target_type=str)
    email=get_input("Email: ", target_type=str)
    phone=get_input("Phone: ", target_type=str)
    note=get_input("Note: ", target_type=str)
    category=get_input("Category: ", target_type=str)

    contact= Contacts(name=name, email=email, phone=phone, note=note, category=category)
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
        note=get_input("Note: ", target_type=str)
        category=get_input("Category: ", target_type=str)

        contact= Contacts(name=name, email=email, phone=phone,note=note,category=category)
        contact.save_file()
        print("Contact is edit successfully.\n")


def category():
    cat_name=input("please enter your category:\n")
    try:
        check=Contacts.search_category(cat_name)
        return(check)
    except:
        return("Category was not found")


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

# def note():
#     contact_name=input("enter contact name:\n")
#     try:
#         check=Contacts.find_by_id(contact_name)
#     except:
#         print("contact was not found!")

#     if check:
#         nte=input("Enter note for contact:\n")
#         finish=Contacts


def page_exit():
    print("Good bye!")
    exit()