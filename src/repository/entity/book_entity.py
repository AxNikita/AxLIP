from sqlalchemy import Column, Integer, String, Numeric, BigInteger, TIMESTAMP, func

from src.repository.entity.base_entity import Base


class BookBase(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String(64), nullable=False)
    book_description = Column(String(255))
    book_link = Column(String(128), nullable=False)
    book_img_link = Column(String(128))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    priority = Column(BigInteger)
    book_page = Column(Numeric)
