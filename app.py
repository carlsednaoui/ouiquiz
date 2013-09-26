'''
These are the basic functions needed to get started.
We can worry about editing and deleting users, questions, answers and quizzes 
at a later date.
'''

import flask
import sqlite3
app = flask.Flask(__name__)

DEBUG = True
app.config.from_object(__name__)

def create_quiz(user_id):
    pass

def create_question(quiz_id):
    pass

def create_answer(question_id):
    pass

def show_quiz(quiz_id):
    pass

@app.route('/create-user', methods=['POST', 'GET'])
def create_user():
    data = flask.request.json
    
    # Save it to DB
    conn = sqlite3.connect('database.db')
    conn.cursor().execute("INSERT INTO users VALUES (?, ?)", [data['email'], data['password']])
    conn.commit()
    conn.close()

    # Call log_in fn
    return flask.jsonify(data)

@app.route('/users')
def list_users():
  users = []

  conn = sqlite3.connect('database.db')
  db_response = conn.cursor().execute("SELECT email FROM users")
  for row in db_response:
    users.append(row)
  conn.close()
  
  return flask.jsonify({"result": users})

def log_in(email, password):
  # Given an email and a password
  # Make sure the user exists
  # Make sure password is correct
  # Return user ID and create session cookie
  pass

'''
To debug:
import ipdb
ipdb.set_trace()
'''

# To create DB
# sqlite3 database.db < schema.sql

'''
Use curl to post data and capture it in the create_user fn.
Once you get the data, do something!

What tool do you need to parse the JSON from the post?

Do you use request.form, request.json or request.data?
Figure out which one to use when.
'''

if __name__ == '__main__':
    app.debug = True
    app.run()
