import unittest
from app.models import User, Category, Post, Comment
from app import db


class CommentModelTest(unittest.TestCase):
    '''
    Class to test the behaviours of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.user_user = User(first_name='John', other_names='Pemba Mwadime',
                              username='pmwadime', email='pemba@ms.com')
        self.new_category = Category(category_name='Fashion')
        self.new_post = Post(post='Unittesting headaches',
                             user_id=1, category_id=1)
        self.new_comment = Comment(
            post_id=1, user_id=1, comments='What an amaizing picth!')

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
        Method that checks if the Comment instance is created
        '''
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        '''
        Method that checks the instance variables
        '''
        self.assertEquals(self.new_comment.post_id, 1)
        self.assertEquals(self.new_comment.user_id, 1)
        self.assertEquals(self.new_comment.comments, 'What an amaizing picth!')

    def test_save_comment(self):
        '''
        Method that checks if the comment instance has been saved
        '''
        self.user_user.save_user()
        self.new_category.save_category()

        # Get the user & category id after save
        user_id = db.session.query(User.id).scalar()
        category_id = db.session.query(Category.id).scalar()

        # Assign the new values to new_post and save
        self.new_post.user_id = user_id
        self.new_post.category_id = category_id
        self.new_post.save_post()

        # Retrieve the post id
        post_id = db.session.query(Post.id).scalar()
        # Assign the new values to the new_comment
        self.new_comment.post_id = post_id
        self.new_comment.user_id = user_id

        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comments(self):
        '''
        Method that checks if records are retrieved by post id
        '''
        self.user_user.save_user()
        self.new_category.save_category()

        # Get the user & category id after save
        user_id = db.session.query(User.id).scalar()
        category_id = db.session.query(Category.id).scalar()

        # Assign the new values to new_post and save
        self.new_post.user_id = user_id
        self.new_post.category_id = category_id
        self.new_post.save_post()

        # Retrieve the post id
        post_id = db.session.query(Post.id).scalar()
        self.new_comment.post_id = post_id
        self.new_comment.user_id = user_id

        self.new_comment.save_comment()

        got_comments = Comment.query.all()
        self.assertTrue(len(got_comments) > 0)