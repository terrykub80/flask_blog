from app import app

@app.route('/')
def index():
    return 'Hello World!!'


@app.route('/posts')
def posts():
    return 'These are the posts'