import praw
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite+pysqlite:///data/reddit.db', echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
Base = declarative_base()

# reddit = praw.Reddit(
#     client_id=
#     client_secret=
#     user_agent=
# )

# Base.metadata.create_all(engine)