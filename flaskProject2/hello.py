from flask import Flask
app = Flask(__name__)
l = []
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/user/<string:username>')
def hello_world1(username):
    l.append(username)
    return f'Added {username} to the list'

@app.route('/user/show')
def hello_world2():

    return f'list : {"".join(l)}'