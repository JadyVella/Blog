from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):
    
    title = StringField('Post title',validators=[Required()])
    content = TextAreaField('Post content',validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):

    comments = TextAreaField('Leave your comment', validators=[Required()])
    submit = SubmitField(' Comment')