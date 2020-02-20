from flask import render_template, url_for, redirect, request, flash, abort
from . import main
from .forms import PostForm, CommentForm
from ..models import User, Post, Comment
from .. import db
from flask_login import login_required

@main.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''

    title = 'Blog'
    message = 'Blog it'

    return render_template('index.html',title = title,message = message)


@main.route('/posts/new', methods = ['GET','POST'])
@login_required
def posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data)
        db.session.add(post)
        db.session.commit()
        
        flash('Your post is create')
        return redirect(url_for('main.index'))
    return render_template('new_posts.html',post_form = form)


@main.route('/view-posts/<int:id>', methods = ['GET','POST'])
@login_required
def view_posts(id):

    posts = Post.query.get(id)

    if posts is None:
        abort(404)


    if form.validate_on_submit():
        comment = Comment.get_comments(id)

    return render_template('view_posts.html',posts = posts, comment = comment)


@main.route('/write_comment', methods=['GET','POST'])
@login_required
def post_comment():

    form = CommentForm()
    title = 'post comment'
    posts = Post.query.filter_by().first()


    return render_template('comment.html', comment_form = form, title = title)
