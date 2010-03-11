"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

from tracking.model import meta

_Base = declarative_base()

def now():
    return datetime.datetime.now()

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine


## Non-reflected tables may be defined and mapped at module level
# Using SQLAlchemy 0.5 optional declarative syntax
# More info here: http://pylonshq.com/docs/en/0.9.7/models/

class Pageviews(_Base):
    __tablename__ = "pageviews"

    st_id = sa.Column(sa.types.Integer, sa.Sequence('page_seq_id', optional=True), primary_key=True)
    st_user_agent = sa.Column(sa.types.String(255), default='')
    st_url = sa.Column(sa.types.String(8000), default='')
    st_spider_date = sa.Column(sa.types.DateTime, default='')
    

## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass

