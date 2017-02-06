from flask import render_template, redirect, request, url_for, flash, jsonify,session
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from .. import db
from app.models.Models import User
from .forms import *
from ..email import send_email
from flask import request

import json

@auth.route('/login', methods=['GET','POST'])
def login():
     pass




@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    new_user = User.create(data)
    session['id'] = hash(new_user['id'])

    return data['username']



# @api.errorhandler(user.ValidationError)
# def handle_user_validation_error(error):
#     response = jsonify({
#         'msg': error.message,
#         'type': 'validation',
#         'field': error.field })
#     response.status_code = 400
#     return response