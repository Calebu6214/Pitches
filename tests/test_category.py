import unittest
from app.models import User, Category, Post, Comment
from app import db


class CategoryModelTest(unittest.TestCase):
    '''
    Class to test the behaviour of the Category class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_category = Category('promotion')

    def tearDown(self):
        '''
        Method that cleans up after every test case run
        '''
        Comment.query.delete()
        Post.query.delete()
        Category.query.delete()
        User.query.delete()

    def test_instance(self):
        '''
        Method that checks if the category instance is created
        '''
        self.assertTrue(isinstance(self.new_category, Category))

    def test_check_instance_variables(self):
        '''
        Method that checks the instance variables
        '''
        self.assertEquals(self.new_category.category_name, 'promotion')

    def test_save_category(self):
        '''
        Method that checks if the instance has been saved.
        '''
        self.new_category.save_category()
        self.assertTrue(len(Category.query.all()) > 0)

    def test_get_categories(self):
        '''
        Method that checks if records are retrieved
        '''
        self.new_category.save_category()
        got_categories = Category.query.all()
        self.assertTrue(len(got_categories) > 0)