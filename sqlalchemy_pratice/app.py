import sqlalchemy
Base = sqlalchemy.ext.declarative_base()

DB_FILE = 'database.db'

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  email = Column(String)
  password = Column(String)

  def __repr__(self):
    return "<User(email='%s', password='%s'>" % (self.email, self.password)

