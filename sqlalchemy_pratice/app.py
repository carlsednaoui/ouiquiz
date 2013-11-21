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

###### START QUERY


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  email = Column(String)
  password = Column(String)
  quizzes = relationship('Quiz')

  def __repr__(self):
    return "<User(email='%s', password='%s'>" % (self.email, self.password)

class Quiz(Base):
  __tablename__ = 'quizzes'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'))
  title = Column(String)


# ipython
# import app
# s = app.Session
# a = s()
# a.query(app.User).all()



# import app
# s = app.Session()
# q = s.query(app.Quiz).all()[0]
# q.user

# Im confused
# http://docs.sqlalchemy.org/en/latest/orm/relationships.html

# NoForeignKeysError: Could not determine join condition between parent/child tables on relationship User.uquizzes - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.