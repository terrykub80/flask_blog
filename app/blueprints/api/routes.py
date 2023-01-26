from flask import request
from . import api
from app.models import Post, User

@api.route('/')
def index():
    return 'Hello this is the API'


# Endpoint to get all of the posts
@api.route('/posts')
def get_posts():
    posts = Post.query.all()
    return [p.to_dict() for p in posts]



# Endpoint to get a single post
@api.route('/posts/<int:post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return post.to_dict()


# Endpoint to create new post
@api.route('/posts', methods=['POST'])
def create_post():
    # Check to see that the request sent a request body that is JSON
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    for field in ['title', 'body', 'user_id']:
        if field not in data:
            # If the field is not in the request body, throw an error saying they are missing that field
            return {'error': f"{field} must be in request body"}, 400

    # pull the fields from the request data
    title = data.get('title')
    body = data.get('body')
    user_id = data.get('user_id')

    # Create a new post with data from request
    new_post = Post(title=title, body=body, user_id=user_id)
    # Return the new post as a JSON respons
    return new_post.to_dict(), 201

    



# Endpoint to get a single user by id
@api.route('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user.to_dict()


# Endpoint to create a new user
@api.route('/users', methods=['POST'])
def create_user():
    # Check to see that the request sent a request body that is JSON
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    data = request.json
    for field in ['username', 'email', 'password']:
        if field not in data:
            # If the field is not in the request body, throw an error saying they are missing that field
            return {'error': f"{field} must be in request body"}, 400
    # pull individual values from the request body
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check to see if there is already a User with that username/email
    existing_user = User.query.filter((User.username == username)|(User.email == email)).first()
    if existing_user:
        return {'error': 'User with this username and/or email already exists'}, 400
    
    # Create a new instance of user
    new_user = User(username=username, email=email, password=password)
    # Send back new user info
    return new_user.to_dict(), 201
    
    
