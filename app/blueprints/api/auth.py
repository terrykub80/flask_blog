from flask_httpauth import HTTPBasicAuth
from app.models import User

basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
def verify(username, password):
    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_password(password):
        return user
    
