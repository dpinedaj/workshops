from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.constants import DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()
