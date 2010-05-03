from sqlalchemy import *
from migrate import *
import migrate.changeset

meta = MetaData(migrate_engine)

pageviews_new = Table('pageviews', meta,
                Column('st_id', Integer, Sequence('page_seq_id', optional=True), primary_key=True),
                Column('st_user_agent', String(255), default=''),
                Column('st_url', String(8000), default=''),
                Column('spider_date', DateTime, default=''),
                )

pageviews_old = Table('pageviews', meta,
                Column('st_id', Integer, Sequence('page_seq_id', optional=True), primary_key=True),
                Column('st_user_agent', String(255), default=''),
                Column('st_url', String(8000), default=''),
                Column('st_spider_date', DateTime, default=''),
                useexisting=True
                )

def upgrade():
    # Upgrade operations go here.
    pageviews_old.c.st_spider_date.alter(name='spider_date')

def downgrade():
    # Operations to reverse the above upgrade go here.
    #col.alter(name='st_spider_date')
    pageviews_new.c.spider_date.alter(name='st_spider_date')