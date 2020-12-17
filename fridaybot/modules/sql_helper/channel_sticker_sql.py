from sqlalchemy import Column, String
from sqlalchemy import Column, LargeBinary, Numeric, UnicodeText
from sql import BASE, SESSION


class Cst(BASE):
    __tablename__ = "cst"
    chat_id = Column(String(14), primary_key=True)
    sticker_token = Column(UnicodeText)

    def __init__(self, chat_id, sticker_token):
        self.chat_id = chat_id
        self.sticker_token = sticker_token


Cst.__table__.create(checkfirst=True)


def add_new_data_in_db(chat_id: int, sticker_token):
    sticker_adder = Cst(str(chat_id), sticker_token)
    SESSION.add(sticker_adder)
    SESSION.commit()


def get_all_st_data(chat_id: int):
    try:
        s__ = SESSION.query(Cst).get(str(chat_id))
        return int(s__.chat_id), s__.sticker_token
    finally:
        SESSION.close()

        
def is_data_indb(chat_id: int):
    try:
        s__ = SESSION.query(Cst).get(str(chat_id))
        if s__:
            return s__.sticker_token
    finally:
        SESSION.close()
        
def remove_data(chat_id):
    s__ = SESSION.query(Cst).get(str(chat_id))
    saved_data = s__.chat_id, s__.sticker_token
    if saved_data:
        SESSION.delete(saved_data)
        SESSION.commit()
