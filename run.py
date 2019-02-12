#!/usr/bin/env python3.6
from core import User # importing the objects to core

def create_user(first_name,last_name,number,usename,password):
    '''
    Function to create a new user's contact
    '''
    new_user = User(first_name,last_name,number,username,password)
    return new_user

def save_users(user):
    '''
    Function to save user's contact
    '''
    user.save_users()

def del_user(contact):
    '''
    Function to delete a contact
    '''
    user.delete_user()

def find_user(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_number(number)

def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your contact list. What is your name?")
            user_name = input()

            print(f"Hello {username}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new user's contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("number ...")
                            p_number = input()

                            print("username")
                            p_number = input()

                            print("password")
                            e_address = input()


                            save_users(create_user(first_name,last_name,number,username,password)) # create and save new contact.
                            print ('\n')
                            print(f"New user {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_user():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_users(search_number):
                                    search_user = find_user(search_number)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"number.......{search_user.number}")
                                    print(f"username.......{search_user.username}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


