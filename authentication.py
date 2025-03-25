from flask import request
from functools import wraps

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        authentication_header = request.headers.get('Authorization')
        if authentication_header != '1234':
            return {"erorr": "Authorization failed"}, 403
        return f(*args, **kwargs)
    return decorated_function

