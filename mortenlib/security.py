import hashlib
from datetime import datetime

#TODO: add debug info

def generate_password_hash(password, debug=False):
    """Return two hex strings. One for hashed password, one for the salt."""
    m = hashlib.sha256()
    salt = hashlib.sha256()
    salt.update(datetime.utcnow().__str__())
    m.update(password)
    m.update(salt.hexdigest())
    
    return m.hexdigest(), salt.hexdigest()

def check_password_hash(password_hash, password, salt, debug=False):
    """Check the hashed password against the real password using given salt"""
    m = hashlib.sha256()
    m.update(password)
    m.update(salt.hexdigest())

    return m.hexdigest() == password_hash 
