'''
These are the basic functions needed to get started.
We can worry about editing and deleting users, questions, answers and quizzes 
at a later date.
'''

import flask
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
    data = flask.request.form
    print data['email']
    return "Returning"

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
