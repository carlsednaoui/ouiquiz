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

    # # Save it to DB via SQL
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

  db_response = Session().query(User.email).all()
  for row in db_response:
    users.append(row)

  return flask.jsonify({'result': users})


@app.route('/login', methods=['POST'])
def log_in():
  data = flask.request.json

  user_email = data['email']
  hashed_password = md5.new(data['password']).hexdigest()

  s = Session()
  res = s.query(User).filter_by(email=user_email, password=hashed_password).all()

  if len(res) == 1:
    return flask.jsonify({'response': 'yes!'})
  else:
    return flask.jsonify({'response': 'go away!'})

  # Return user ID and create session cookie


@app.route('/create-quiz', methods=['POST'])
def create_quiz():
  """
  Requires email, title
  """
  data = flask.request.json
  
  s = Session()
  _user_id = s.query(User.id).filter_by(email=data['email']).all()[0]
  quiz = Quiz(user_id = str(_user_id), title = data['title'])
  s.add(quiz)
  s.commit()

  return flask.jsonify({'email': data['email'], 'title': data['title']})


@app.route('/quizzes')
def get_quizzes():
  quizzes = []

  db_response = Session().query(Quiz.title).all()
  for row in db_response:
    quizzes.append(row)

  return flask.jsonify({'result': quizzes})


@app.route('/create-question', methods=['POST'])
def create_question():
  data = flask.request.json

  s = Session()
  question = Question(quiz_id = data['quiz_id'], title = data['title'])
  s.add(question)
  s.commit()

  return flask.jsonify({'quiz_id': data['quiz_id'], 'title': data['title']})


@app.route('/questions')
def get_questions():
  questions = []

  db_response = Session().query(Question.title).all()
  for row in db_response:
    questions.append(row)

  return flask.jsonify({'result': questions})


if __name__ == '__main__':
    app.debug = True
    app.run()
