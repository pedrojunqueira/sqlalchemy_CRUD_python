# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql://usr:pass@localhost:5434/sqlalchemy') # docker connections
engine = create_engine('postgresql://pedrojunqueira:pass@localhost:5432/sqlalchemy') # local connections
Session = sessionmaker(bind=engine)

Base = declarative_base()
