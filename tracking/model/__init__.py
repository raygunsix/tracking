"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from tracking.model import meta

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
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)
pageviews_table = sa.Table('pageviews', meta.metadata,
               sa.schema.Column('id', sa.types.Integer,
                   sa.schema.Sequence('page_seq_id', optional=True), primary_key=True),
                sa.Column('content_id', sa.types.Integer, default=''),
                sa.Column('object_id', sa.types.Integer, default=''),
                sa.Column('search_terms', sa.types.String, default=''),
                sa.Column('referrer', sa.types.String, default=''),
                sa.Column('user_agent', sa.types.String, default=''),
                sa.Column('create_date', sa.types.DateTime, default='')
                )

## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
class Pageviews(object):

    def __str(self):
        return self.article_id

orm.mapper(Pageviews, pageviews_table)
