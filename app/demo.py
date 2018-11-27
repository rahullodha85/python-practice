from flask import request, render_template, make_response, abort

from app import app


@app.route('/')
def index():
    return "Hello, this is home page!"

@app.route('/test')
def hello_test():
    return 'Hello, Test!'

@app.route("/user")
def user():
    val = "Hello World!"
    username = request.headers.get("username")
    resp = make_response(render_template('hello.html', name=username))
    resp.set_cookie('username', username)
    resp.headers['username'] = username
    return resp

@app.route('/debug')
def hello_debug():
    return 'Hello, Debug!'

@app.route('/<myVal>')
def print_myVal(myVal):
    return 'Hello, %s!' %myVal

@app.route('/login')
def login():
    abort(401)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)