from datetime import datetime
# import hashlib
# from werkzeug.security import generate_password_hash, check_password_hash
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from markdown import markdown
# import bleach
# from flask import current_app, request, url_for
# from flask_login import UserMixin, AnonymousUserMixin
# from app.exceptions import ValidationError
from .. import db, login_manager
from . import Base, mixins