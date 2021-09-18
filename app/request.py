# import urllib.request,json
from . import db
from sqlalchemy import desc
from .models import Post, PostDetails, Category, User, Comment, CommentDetails

def get_posts(cid):
    '''
    Function that retrieves posts
    '''
    if cid == 0:
        results = db.session.query(Post, Category, User). \
            select_from(Post).join(Category).join(
                User).order_by(desc(Post.id)).all()
    else:
        results = db.session.query(Post, Category, User). \
            select_from(Post).join(Category).join(User).filter(
                Post.category_id == cid).order_by(desc(Post.id)).all()

    comments = get_comments()

    post_details = []

    for post, category, user in results:
        post_id = post.id
        post_date = post.created_at
        post_detail = post.post
        category = category.category_name
        posted_by = user.first_name+" "+user.other_names
        profile_pic_path = user.profile_pic_path
        upvote = post.upvote
        downvote = post.downvote

        count = 0
        if comments:
            for comment in comments:
                if comment.post_id == post_id:
                    count += 1

        post_detail_object = PostDetails(
            post_id, post_date, post_detail, category, posted_by, profile_pic_path, count, upvote, downvote)
        post_details.append(post_detail_object)
        count = 0
    return post_details


def get_comments():
    '''
    Function that retrieves comments
    '''
    results = db.session.query(Comment, User). \
            select_from(Comment).join(User).order_by(desc(Comment.id)).all()
    
    comments = []

    for comment, user in results:
        post_id = comment.post_id
        comments_made = comment.comments
        comment_date = comment.created_at
        commented_by = user.first_name+" "+user.other_names
        profile_pic_path = user.profile_pic_path

        comments_object = CommentDetails(
            post_id, comments_made, comment_date, commented_by, profile_pic_path)
        comments.append(comments_object)

    return comments

def get_posts_by_user_id(userid):
    '''
    Function that retrieves posts by id
    '''
    results = db.session.query(Post, Category, User). \
        select_from(Post).join(Category).join(User).filter(
        Post.user_id == userid).order_by(desc(Post.id)).all()

    comments = get_comments()

    post_details = []

    for post, category, user in results:
        post_id = post.id
        post_date = post.created_at
        post_detail = post.post
        category = category.category_name
        posted_by = user.first_name+" "+user.other_names
        profile_pic_path = user.profile_pic_path
        upvote = post.upvote
        downvote = post.downvote


        count = 0
        if comments:
            for comment in comments:
                if comment.post_id == post_id:
                    count += 1

        post_detail_object = PostDetails(
            post_id, post_date, post_detail, category, posted_by, profile_pic_path, count, upvote, downvote)
        post_details.append(post_detail_object)
        count = 0
    return post_details

def get_posts_by_post_id(pid):
    '''
    Function that retrieves posts by id
    '''
    post = Post.get_post_by_id(pid)
    category = Category.get_category_by_id(post.category_id)
    comments = get_comments()
    user = User.query.filter_by(id=post.user_id).first()

    post_id = post.id
    post_date = post.created_at
    post_detail = post.post
    category = category.category_name
    posted_by = user.first_name+" "+user.other_names
    profile_pic_path = user.profile_pic_path
    upvote = post.upvote
    downvote = post.downvote


    count = 0
    if comments:
        for comment in comments:
            if comment.post_id == post_id:
                count += 1

    
    post_details = PostDetails(
        post_id, post_date, post_detail, category, posted_by, profile_pic_path, count, upvote, downvote)
    

    count = 0

    return post_details



