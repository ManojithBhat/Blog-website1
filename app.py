from flask import Flask,render_template,flash,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, validators,TextAreaField
from utils import languages,translate_text
from dotenv import load_dotenv
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_PASS")
app.config['SECRET_KEY'] = os.getenv("PASSWORD")

db = SQLAlchemy(app)

#creating model for storing blog post details 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(20), nullable=False)
    heading = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50),nullable=False,default="AUTHOR")

    def __repr__(self):
        return f"Post('{self.language}', '{self.heading}','{self.author}')"
    
#form for recieving the blog post 
class PostForm(FlaskForm):
    title = StringField('Title',validators=[validators.DataRequired()])
    content = TextAreaField('Content',validators=[validators.DataRequired()])
    language = StringField('language',validators=[validators.DataRequired()])
    author = StringField("author",validators=[validators.DataRequired()])
    submit = SubmitField('submit')


language_choices = []
for key,value in languages.items():
    language_choices.append((key,value))


class LanguageForm(FlaskForm):
    language_field = SelectField("Language to translate to",choices=language_choices,default='en')
    submit = SubmitField("Translate")

#home route
@app.route('/',methods=['GET', 'POST'])
def index():
    form = PostForm()

    if form.validate_on_submit():

        #taking input from the form and storing in the database
        new_post = Post(
            language=form.language.data,
            heading=form.title.data,
            body=form.content.data,
            author=form.author.data
        )

        db.session.add(new_post)
        db.session.commit()
        #show a flash message in the home when blog post is created
        flash('your post has been created','success')

        form.language.data = ''
        form.title.data = ''
        form.content.data = ''
        form.author.data=''

    posts = Post.query.all()

    return render_template("index.html",posts = posts,form=form)

#blog post route 
@app.route('/post/<int:id>',methods=['POST','GET'])
def post(id):
    form = LanguageForm()
    post = Post.query.get(id)

    if form.validate_on_submit():
        language = form.language_field.data
        post.heading = translate_text(post.heading,language).text
        post.author = translate_text(post.author,language).text
        post.language = languages[language]
        post.body = translate_text(post.body,language).text

    return render_template('post.html',post=post,form=form)

if __name__ == "__main__":
    app.run(debug=True)