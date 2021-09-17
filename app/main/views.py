from flask import render_template, redirect, url_for, request, abort
# from flask_login import login_required, current_user
from . import main
from .forms import PostForm, AddComment, UpdateProfile
from ..auth.forms import LoginForm, RegistrationForm
from ..models import User, Post, Category, Comment
from ..request import get_posts, get_comments, get_posts_by_user_id, get_posts_by_post_id
from ..import db, photos
from sqlalchemy import func


@main.route('/')
def index():
    '''
    View function that returns the index page
    '''
    title = "Pitches-Welcome to pitch site"
    return render_template('index.html', title=title)

@main.route('/home/<int:cid>', methods=['GET'])
# @login_required
def home(cid):
    '''
    View function that returns the home page
    '''

    categories = Category.get_categories()
    posts = get_posts(cid)

    if cid == 0:
        category_name = "All Categories"
    else:
        selected_category = Category.get_category_by_id(cid)
        category_name = selected_category.category_name

    post_form = PostForm()

    title = 'Pitches'

    return render_template('home.html', post_form=post_form, title=title, posts=posts, categories=categories, category_name=category_name, )