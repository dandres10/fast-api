import os 
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


""" sqliteName = 'movies.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
datebaseUrl = f"sqlite:///{os.path.join(base_dir, sqliteName)}"


engine = create_engine(datebaseUrl, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base() """


# Reemplaza los valores de usuario, contraseña, host, puerto y nombre_bd con los de tu configuración
engine = create_engine('postgresql+psycopg2://postgres:marlon@localhost:5432/goluti_dev')
Session = sessionmaker(bind=engine)
Base = declarative_base()
