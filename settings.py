import os
from dotenv import load_dotenv
load_dotenv()

# Secret key setting from .env for Flask sessions
SECRET_KEY = b'\xb9&P\xd8\xb3\xba\xc4\xdf\xe5\x97\x88)h\xf9\xc9\xd3'

# DB base configuration from .env for modularity and security reasons
DB = {
    'host' : os.environ.get('localhost'),
    'user': os.environ.get('root'),
    'password': os.environ.get('root'),
    'database': os.environ.get('DB_NAME')
}
