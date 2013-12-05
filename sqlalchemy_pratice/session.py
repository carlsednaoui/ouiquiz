In [1]: import app

In [2]: s = app.Session()

In [3]: user = app.User()

In [4]: user.email = "carl123@example.com"

In [5]: user.password = "foo"

In [6]: user
Out[6]: <User(email='carl123@example.com', password='foo'>

In [7]: s.add(user)

In [8]: s.query(app.User).all
Out[8]: <bound method Query.all of <sqlalchemy.orm.query.Query object at 0x10432f850>>

In [9]: s.query(app.User).all()
Out[9]: 
[<User(email='carl_1@example.com', password='secure'>,
 <User(email='carl_2@example.com', password='secure'>,
 <User(email='carl_3@example.com', password='secure'>,
 <User(email='carl123@example.com', password='foo'>]

In [10]: s.query(app.User).all()
Out[10]: 
[<User(email='carl_1@example.com', password='secure'>,
 <User(email='carl_2@example.com', password='secure'>,
 <User(email='carl_3@example.com', password='secure'>,
 <User(email='carl123@example.com', password='foo'>]

In [11]: exit
(venv)⚡ carl@book sqlalchemy_pratice (master) ipython
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43) 
Type "copyright", "credits" or "license" for more information.

IPython 1.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import app

In [2]: s = app.Session()

In [3]: s.query(app.User).all()
Out[3]: 
[<User(email='carl_1@example.com', password='secure'>,
 <User(email='carl_2@example.com', password='secure'>,
 <User(email='carl_3@example.com', password='secure'>]

In [4]: user = app.User

In [5]: user = app.User(email = 'carl123@ex.com', password = 'foo')

In [6]: user
Out[6]: <User(email='carl123@ex.com', password='foo'>

In [7]: s
Out[7]: <sqlalchemy.orm.session.Session at 0x1042e26d0>

In [8]: s.add(user)

In [9]: s.query(app.User).all()
Out[9]: 
[<User(email='carl_1@example.com', password='secure'>,
 <User(email='carl_2@example.com', password='secure'>,
 <User(email='carl_3@example.com', password='secure'>,
 <User(email='carl123@ex.com', password='foo'>]

In [10]: s
%%script      %%sx          %sc           %system       setattr       staticmethod  super         
%%sh          %%system      %store        s             slice         str           
%%svg         %save         %sx           set           sorted        sum           

In [10]: s
%%script      %%sx          %sc           %system       setattr       staticmethod  super         
%%sh          %%system      %store        s             slice         str           
%%svg         %save         %sx           set           sorted        sum           

In [10]: s.d
s.delete    s.deleted   s.dirty     s.dispatch  

In [10]: s.di
s.dirty     s.dispatch  

In [10]: s.dirty
Out[10]: IdentitySet([])

In [11]: s.dirty
s.dirty

In [11]: s.dirty
s.dirty

In [11]: s.dirty
Out[11]: IdentitySet([])

In [12]: s.commit()

In [13]: user
Out[13]: <User(email='carl123@ex.com', password='foo'>

In [14]: user.id
Out[14]: 4

In [15]: user = app.User(email = 'carl1234@ex.com', password = 'foo')

In [16]: user.id

In [17]: s.di
s.dirty     s.dispatch  

In [17]: s.dirty
Out[17]: IdentitySet([])

In [18]: s.dirty()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-d0f580e874db> in <module>()
----> 1 s.dirty()

TypeError: 'IdentitySet' object is not callable

In [19]: s.commit()

In [20]: s
Out[20]: <sqlalchemy.orm.session.Session at 0x1042e26d0>

In [21]: user.id

In [22]: user.id

In [23]: s.add(user)

In [24]: user.id

In [25]: s.commit()

In [26]: user.id
Out[26]: 5

In [27]: user.password = "bar"

In [28]: s.dirty
Out[28]: IdentitySet([<User(email='carl1234@ex.com', password='bar'>])

In [29]: s.commit()

In [30]: s.dirty
Out[30]: IdentitySet([])

In [31]: s
%%script      %%sx          %sc           %system       setattr       staticmethod  super         
%%sh          %%system      %store        s             slice         str           
%%svg         %save         %sx           set           sorted        sum           

In [31]: s
%%script      %%sx          %sc           %system       setattr       staticmethod  super         
%%sh          %%system      %store        s             slice         str           
%%svg         %save         %sx           set           sorted        sum           

In [31]: s.
s.add                          s.deleted                      s.is_active
s.add_all                      s.dirty                        s.is_modified
s.autocommit                   s.dispatch                     s.merge
s.autoflush                    s.enable_relationship_loading  s.new
s.begin                        s.execute                      s.no_autoflush
s.begin_nested                 s.expire                       s.object_session
s.bind                         s.expire_all                   s.prepare
s.bind_mapper                  s.expire_on_commit             s.prune
s.bind_table                   s.expunge                      s.public_methods
s.close                        s.expunge_all                  s.query
s.close_all                    s.flush                        s.refresh
s.commit                       s.get_bind                     s.rollback
s.connection                   s.hash_key                     s.scalar
s.connection_callable          s.identity_key                 s.transaction
s.delete                       s.identity_map                 s.twophase

In [31]: q = app.Quiz(user_id = user.id, title = "alchemy quiz")

In [32]: s.query(app.Quiz).all()
Out[32]: 
[<app.Quiz at 0x1043ca410>,
 <app.Quiz at 0x1043ca650>,
 <app.Quiz at 0x1043ca710>,
 <app.Quiz at 0x1043ca7d0>,
 <app.Quiz at 0x1043ca890>,
 <app.Quiz at 0x1043ca950>,
 <app.Quiz at 0x1043caa10>]

In [33]: s.query(app.Quiz).all().length
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-33-ebdfcca16975> in <module>()
----> 1 s.query(app.Quiz).all().length

AttributeError: 'list' object has no attribute 'length'

In [34]: s.query(app.Quiz).all().count
Out[34]: <function count>

In [35]: s.query(app.Quiz).all().count()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-298398c4bf0d> in <module>()
----> 1 s.query(app.Quiz).all().count()

TypeError: count() takes exactly one argument (0 given)

In [36]: count(s.query(app.Quiz).all())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-36-0876933cc9c4> in <module>()
----> 1 count(s.query(app.Quiz).all())

NameError: name 'count' is not defined

In [37]: len(s.query(app.Quiz).all())
Out[37]: 7

In [38]: s.add(a)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-38-078bdd6fa94e> in <module>()
----> 1 s.add(a)

NameError: name 'a' is not defined

In [39]: s.add(q)

In [40]: len(s.query(app.Quiz).all())
Out[40]: 8

In [41]: s.commit()

In [42]: len(s.query(app.Quiz).all())
Out[42]: 8

In [43]: s.query(app.Quiz).all()
Out[43]: 
[<app.Quiz at 0x1043ca410>,
 <app.Quiz at 0x1043ca650>,
 <app.Quiz at 0x1043ca710>,
 <app.Quiz at 0x1043ca7d0>,
 <app.Quiz at 0x1043ca890>,
 <app.Quiz at 0x1043ca950>,
 <app.Quiz at 0x1043caa10>,
 <app.Quiz at 0x104366b90>]

In [44]: q.id
Out[44]: 8

In [45]: q.user
Out[45]: <User(email='carl1234@ex.com', password='bar'>

In [46]: q.user.id
Out[46]: 5

In [47]: q.user.quizzes
Out[47]: [<app.Quiz at 0x104366b90>]