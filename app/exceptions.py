from flask import jsonify

class ValidationError(Exception):
    def __init__(self,field, message):
        self.field = field
        self.message= message