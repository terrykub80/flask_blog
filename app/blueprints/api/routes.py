from . import api
from app.models import Post

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
