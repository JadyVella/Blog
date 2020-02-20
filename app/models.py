from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    users = db.relationship('User', backref = 'post',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'comments',lazy = "dynamic")

    def save_post(self):
        """
        Save posts 
        """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_posts(cls):
        Pitch.all_posts.clear()

    # display posts

    def get_posts(cat_id):
        posts = Post.query.filter_by(posts.id).all()
        return posts


    def __repr__(self):
        return f'Post {self.title}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(),index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))


    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments


    def __repr__(self):
        return f'Comment {self.comment}'

