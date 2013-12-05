'''
These are the basic functions needed to get started.
We can worry about editing and deleting users, questions, answers and quizzes 
at a later date.
'''

import flask
import sqlite3
import md5
from models import User, Quiz, Question, Session

app = flask.Flask(__name__)

DEBUG = True
app.config.from_object(__name__)

@app.route('/create-user', methods=['POST', 'GET'])
def create_user():
    data = flask.request.json
    m = md5.new()

    m.update(data['password'])
    hashed_password = m.hexdigest()

    # # Save it to DB
    # conn = sqlite3.connect('database.db')
    # conn.cursor().execute("INSERT INTO users VALUES (?, ?)", [data['email'], hashed_password])
    # conn.commit()
    # conn.close()

    s = Session()
    user = User(email = data['email'], password = hashed_password)
    s.add(user)
    s.commit()

    # Call log_in fn
    return flask.jsonify({'email': data['email'], 'password': hashed_password})

@app.route('/users')
def list_users():
  users = []

  conn = sqlite3.connect('database.db')
  db_response = conn.cursor().execute("SELECT email FROM users")
  for row in db_response:
    users.append(row)
  conn.close()
  
  return flask.jsonify({'result': users})

@app.route('/login', methods=['POST'])
def log_in():
  data = flask.request.json

  email = data['email']
  hashed_password = md5.new(data['password']).hexdigest()

  conn = sqlite3.connect('database.db')
  db_response = conn.cursor().execute("SELECT email FROM users WHERE email = ? AND password = ?", [email, hashed_password])

  if len(db_response.fetchall()) == 1:
    conn.close()
    return flask.jsonify({'response': 'yes!'})
  else:
    conn.close()
    return flask.jsonify({'response': 'go away!'})

  # Return user ID and create session cookie

@app.route('/create-quiz', methods=['POST'])
def create_quiz():
  """
  Requires email, title
  """
  data = flask.request.json
  conn = sqlite3.connect('database.db')
  user_id = conn.cursor().execute("SELECT id FROM users WHERE email = ?", [data['email']])
  conn.cursor().execute("INSERT INTO quizzes ('user_id', 'title') VALUES (?, ?)", [str(user_id), data['title']])
  conn.commit()
  conn.close()

  return flask.jsonify({'email': data['email'], 'title': data['title']})

@app.route('/quizzes')
def get_quizzes():
  quizzes = []

  conn = sqlite3.connect('database.db')
  db_response = conn.cursor().execute("SELECT title FROM quizzes")
  for row in db_response:
    quizzes.append(row)
  conn.close()

  return flask.jsonify({'result': quizzes})

@app.route('/create-question', methods=['POST'])
def create_question():
  data = flask.request.json

  conn = sqlite3.connect('database.db')
  conn.cursor().execute("INSERT INTO questions ('quiz_id', 'title') VALUES (?, ?)", [data['quiz_id'], data['title']])
  conn.commit()
  conn.close()

  return flask.jsonify({'quiz_id': data['quiz_id'], 'title': data['title']})

@app.route('/questions')
def get_questions():
  questions = []

  conn = sqlite3.connect('database.db')
  db_response = conn.cursor().execute("SELECT title FROM questions")
  for row in db_response:
    questions.append(row)
  conn.close()

  return flask.jsonify({'result': questions})


if __name__ == '__main__':
    app.debug = True
    app.run()
