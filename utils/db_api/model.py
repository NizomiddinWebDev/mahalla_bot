from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:1234@localhost/bot_db', echo=True)
# engine = create_engine('mysql+pymysql://nizom:nizom0299@localhost:3306/web_bot', echo=True)

Base = declarative_base()

meta = MetaData()

check = Table(
    'mahalla_bot', meta,
    Column('chat_id', String(200), primary_key=True),
    Column('types', String(200)),
    Column('state', String(20)),
    Column('full_name', String(200)),
)
meta.create_all(engine)


class Customers(Base):
    __tablename__ = 'mahalla_bot'

    chat_id = Column(String, primary_key=True)
    types = Column(String)
    state = Column(String)
    full_name = Column(String)


async def new_user_add(chat_id, types, state, full_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    customer = Customers(
        chat_id=chat_id,
        types=types,
        state=state,
        full_name=full_name
    )
    session.add(customer)
    session.commit()


async def getUserList():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.types == "user")
    return result


async def getGroupList():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.types == "group").all()
    return result


async def getUsersCount():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.types == "user").count()
    return result


async def getGroupsCount():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.types == "group").count()
    return result


async def getUserLang(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.chat_id == str(user_id)).one()
    return result


async def setUserLang(user_id, lang):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Customers).filter(Customers.chat_id == str(user_id)).update({Customers.lang: lang})
    session.commit()


async def get_user_name(full_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Customers).filter(Customers.full_name == full_name).one()
    return result
