from app import app
from flask import render_template
from app.forms import SignUpForm

@app.route('/')
def index():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'mango', 'blueberry']
    return render_template('index.html', name='Terry', fruits=fruits)
    


@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/signup')
def signup():
    # Create an instance of the SignUpForm
    form = SignUpForm()
    return render_template('signup.html', form=form)

