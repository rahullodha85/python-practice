from flask import Flask, request, render_template, make_response
app = Flask(__name__)

@app.route('/')
def index():
    val = "Hello World!"
    username = request.headers.get("username")
    val = val + "\n" + "Hello %s!" %username
    resp = make_response(render_template('hello.html', name=username))
    resp.set_cookie('username', username)
    resp.headers['username']=username
    return resp

@app.route('/test')
def hello_test():
    return 'Hello, Test!'

@app.route('/debug')
def hello_debug():
    return 'Hello, Debug!'

@app.route('/<myVal>')
def print_myVal(myVal):
    return 'Hello, %s!' %myVal

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "This is a response for login POST request!"
    else:
        return 'This is login form!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)