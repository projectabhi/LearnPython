from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

from database import Base, session, engine


class User(Base):
    __tablename__ = "user"
    id = Column('id',Integer,primary_key=True)
    username = Column('username',String(20),unique=True)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User({self.id},{self.username}),{self.posts}"
    

class Post(Base):
    __tablename__ = "post"
    id = Column('id',Integer, primary_key=True)
    title = Column('title',String(100), nullable=False)
    date_posted = Column('date',DateTime, nullable=False, default=datetime.utcnow())
    content = Column('content',Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    

Base.metadata.create_all(bind=engine)
usersession = session()
# user = User()
# user.id = 2
# user.username = 'Test'
#
# usersession.add(user)
# usersession.commit()
#
user = usersession.query(User).get(1)
user.username='bubai'

post1 = Post()
post1.id = 1
post1.content = 'Test content 1'
post1.title = 'Test title 1'

post2 = Post()
post2.id = 2
post2.content = 'Test content 2'
post2.title = 'Test title 2'

# user.posts = ([post1,post2])
#
# usersession.add(user)
# usersession.commit()
users = usersession.query(User).all()
for user in users:
    print(user)

usersession.close()
Base.metadata.drop_all(bind=engine)