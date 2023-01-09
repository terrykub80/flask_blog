from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', name='Terry')


@app.route('/posts')
def posts():
    return 'These are the posts'

