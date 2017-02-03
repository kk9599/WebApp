from flask import render_template, redirect, request, url_for, flash, jsonify
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




@auth.route('/register', methods=['GET','POST'])
def register():
    data = request.get_json()

    return data
