import unittest # Importing the unittest module
from core import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_user = User("paccy","mucyo","0788492346","mucyopaccy","pacco")

    def test_init(self):
        """
        test if the object entered
        """
        self.assertEqual(self.new_user.first_name,"paccy")
        self.assertEqual(self.new_user.last_name,"mucyo")
        self.assertEqual(self.new_user.number,"0788492346")
        self.assertEqual(self.new_user.username,"mucyopaccy")
        self.assertEqual(self.new_user.password,"pacco")  

    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''

        self.new_user.save_user()#saving new contact 
        self.assertEqual(len(User.user_list),1) 

# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here

    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = User("caline","paccy","0723456789","calinepaccy","caline") # new contact
        test_user.save_user()
        self.assertEqual(len(User.user_list),2) 

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("caline","paccy","0723456789","calinepaccy","caline") # new contact
        test_user.save_user()

        User_exists = User.User_exist("0723456789")

        self.assertTrue(User_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

    def test_delete_contact(self):

        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_user.save_user()
        test_user = User("caline","paccy","0723456789","calinepaccy","caline") # new contact
        test_user.save_user()

        self.new_user.delete_user()# Deleting a contact object
        self.assertEqual(len(User.user_list),1) 

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("caline","paccy","0723456789","calinepaccy","caline") # new contact
        test_user.save_user()

        found_user = User.find_by_number("0723456789")

        self.assertEqual(found_user.username,test_user.username)

if __name__ == '__main__':
    unittest.main()


    
          