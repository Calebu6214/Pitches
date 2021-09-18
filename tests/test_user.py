import unittest
from app.models import User


class UserModelTest(unittest.TestCase):
    '''
    Class to test the behaviour of the User class.
    '''

    def setUp(self):
        '''
        Set up method that will run before every test by creating an
        instance of the User class.
        '''
        self.new_user = User(password='banana')

    def test_password_setter(self):
        '''
        Test case to ascertain that the password is being harshed and that
        the password_has contains a value.
        '''
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        '''
        Test case to confirm if the application raises an AttributeError when we
        try to access the password property.
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Test case to confirm that the password_hash can be verified when we pass the 
        correct password.
        '''
        self.assertTrue(self.new_user.verify_password('banana'))