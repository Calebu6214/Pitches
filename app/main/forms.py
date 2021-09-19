
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, validators
from wtforms_sqlalchemy.fields import QuerySelectField
from sqlalchemy.orm.util import identity_key
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from wtforms.fields import SelectFieldBase
from ..models import Category
from wtforms import ValidationError
from  wtforms.validators import Required,EqualTo,Email
from flask_sqlalchemy import SQLAlchemy
# from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField

has_identity_key = True

__all__ = (
    'QuerySelectField', 'QuerySelectMultipleField',
)
# class ReviewForm(FlaskForm):

#     title=StringField('Pitch title', validators=[Required()])
#     review=TextAreaField('pitch text..')
#     submit=SubmitField('Add Pitch')

class UpdateProfile(FlaskForm):
    '''
    Class to create an update profile form
    '''
    first_name = StringField("First name", validators=[Required()])
    other_names = StringField("Other names", validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    '''
    Class to create a post form
    '''
    def category_query():
        return Category.query

    category = QuerySelectField(query_factory = category_query,blank_text="Select category", get_label='category_name',validators=[validators.DataRequired()])
    post = TextAreaField('Your post here...',  validators=[Required()])
    endpoint = StringField('Endpoint', validators=[Required()])
    submit = SubmitField('Post')

class AddComment(FlaskForm):
    '''
    Class to create add comment form
    '''
    comment = StringField('Add comment', validators=[Required()])
    submit = SubmitField('Add')
