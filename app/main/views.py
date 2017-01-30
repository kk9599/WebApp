from flask import render_template, redirect, url_for, abort, flash, request, current_app, make_response, send_file
from . import main


@main.route('/', methods=['GET','POST'])
def index():
    return send_file("templates/index.html")


@main.route('/js/<path:jsfile>.js', methods=['GET'])
def send_js(jsfile):
    return send_file("static/js/{0}.js".format(jsfile))


@main.route('/img/<path:imgFile>',methods=['GET'])
def send_img(imgFile):
    return send_file("static/img/{0}".format(imgFile))

@main.route('/shutdown')
def server_shutdown():
    shutdown = request.environ.get('werkzeug.server.shutdown')
    shutdown()
    return 'shuting down....'