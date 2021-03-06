from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User
from werkzeug.security import check_password_hash

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    u = User.query.filter_by(username=username).first()
    if u and check_password_hash(u.password, password):
        return u
    return None

