import sqlalchemy as sa

# import base from meta class
from tracking.model.meta import Base 

# Using SQLAlchemy 0.5 optional declarative syntax
# More info here: http://pylonshq.com/docs/en/0.9.7/models/
# and here: http://pylonshq.com/pasties/1000

class Pageviews(Base):
    __tablename__ = "pageviews"

    st_id = sa.Column(sa.types.Integer, sa.Sequence('page_seq_id', optional=True), primary_key=True)
    st_user_agent = sa.Column(sa.types.String(255), default='')
    st_url = sa.Column(sa.types.String(8000), default='')
    st_spider_date = sa.Column(sa.types.DateTime, default='')

