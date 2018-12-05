from flask import request, render_template, make_response, abort, Blueprint

demo = Blueprint('demo_bblueprint', __name__)

@demo.route('/')
def index():
    return "Hello, this is home page!"

@demo.route('/test')
def hello_test():
    return 'Hello, Test!'

@demo.route("/user")
def user():
    val = "Hello World!"
    username = request.headers.get("username")
    resp = make_response(render_template('hello.html', name=username))
    resp.set_cookie('username', username)
    resp.headers['username'] = username
    return resp

@demo.route('/debug')
def hello_debug():
    return 'Hello, Debug!'

@demo.route('/<myVal>')
def print_myVal(myVal):
    return 'Hello, %s!' %myVal

@demo.route('/login')
def login():
    abort(401)

@demo.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@demo.route('/hello/')
@demo.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)