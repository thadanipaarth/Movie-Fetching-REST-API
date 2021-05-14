"""
Authentication module
"""

import connexion
from jose import JWTError, jwt
import six
from werkzeug.exceptions import Unauthorized

# JSON Web Token Configuration 
JWT_ISSUER = 'Movies API'
JWT_SECRET = 'thisismyrestapi' # Secret key used to encode and decode the token
JWT_LIFETIME_SECONDS = 365*24*60*60 # Lifetime of the token in seconds
JWT_ALGORITHM = 'HS256'

def decode_token(apikey, required_scopes=None):
    """
        Purpose: Verifies that JSON Web Token can be decoded using the JSW_SECRET
        Parameters: - apikey
                    - required_scopes (optional)
    """
    try:
        return jwt.decode(apikey, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)