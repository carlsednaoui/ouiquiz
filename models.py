import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

DB_FILE = 'database.db'
Base = declarative_base()

# This is how we connect to the DB
db_string = 'sqlite:///{0}'.format(DB_FILE)
e = sqlalchemy.create_engine(db_string)

# Create tables, if needed
Base.metadata.create_all(e)

# Create session
Session = sqlalchemy.orm.sessionmaker(bind=e)

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  email = Column(String)
  password = Column(String)

  def __repr__(self):
    return "<User(email='%s', password='%s'>" % (self.email, self.password)

class Quiz(Base):
  __tablename__ = 'quizzes'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  title = Column(String)
  user = relationship('User', backref=backref('quizzes'))

class Question(Base):
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  quiz_id = Column(Integer, ForeignKey('quizzes.id'))
  title = Column(String)
  quiz = relationship('Quiz', backref=backref('questions'))


# ipython
# import app
# s = app.Session()
# q = s.query(app.Quiz).all()[0]
# q.user