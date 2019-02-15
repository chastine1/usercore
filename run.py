#!/usr/bin/env python3.6
from core import User # importing the objects to core
# import ptvsd


def create_user(first_name,last_name,number,username,password):
    '''
    Function to create a new user's contact
    '''
    new_user = User(first_name,last_name,number,username,password)
    return new_user

def save_user(user):
    '''
    Function to save user's contact
    '''
    user.save_user()

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

def User_exist(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.User_exist(number)

def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    userName = input()

    print(f"Hello {userName}. what would you like to do?")
    print('\n')

    while True:
                print("Use these short codes : cc - create a new user's contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                short_code = input().lower()

                if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            first_name = input()

                            print("Last name ...")
                            last_name = input()

                            print("number ...")
                            number = input()

                            print("username")
                            username = input()

                            print("password")
                            password = input()


                            save_user(create_user(first_name,last_name,number,username,password)) # create and save new contact.
                            print ('\n')
                            print(f"New user {first_name} {last_name} {number} {username} {password} created")
                            print ('\n')

                elif short_code == 'dc':

                        if display_users():
                                print("Here is a list of all your contacts")
                                print('\n')

                                for user in display_users():
                                    print(f"{user.first_name} {user.last_name} {user.number} {user.username} {user.password}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any contacts saved yet")
                                print('\n')

                elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if User_exist(search_number):
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


if __name__ == '__main__':

    main()