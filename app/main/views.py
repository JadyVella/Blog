from flask import render_template, url_for, redirect, request
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
    return render_template('posts.html',form = form, post = post)