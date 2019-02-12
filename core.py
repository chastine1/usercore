class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] # Empty contact list


    def __init__(self,first_name,last_name,number,username,password):
        #creating an email
    
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.username = username
        self.password = password

    user_list = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)
  


    @classmethod
    def User_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.number == number:
                    return True

        return False

    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.number == number:
                return user

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list
