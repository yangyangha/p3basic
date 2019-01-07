from flask import Flask, url_for
app = Flask(__name__)

'''
http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
'''
'''
  basic 
'''


@app.route('/hi')
def hello_world():
    return 'Hello World!'


@app.route("/")
def hello():
    return "Hello World!"


'''
    Variable Rules
'''


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == '__main__':
    app.debug = True
    app.run()