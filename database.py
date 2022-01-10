
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://bdjipanm:6TsnnNAj-BuI0glXYHAS-QB7RTwFELXx@abul.db.elephantsql.com/bdjipanm")
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()