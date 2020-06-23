import jwt,os
from flask import jsonify,request
from functools import wraps

def Key_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        Key = None

        if 'x-access-Key' in request.headers:
            Key = request.headers['x-access-Key']

        try: 
            data = jwt.decode(os.getenv('Token'),Key)
        except:
            return jsonify({'message' : 'Permission is denied to access the API'}), 401

        return f(*args, **kwargs)

    return decorated