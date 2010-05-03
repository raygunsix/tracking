from sqlalchemy import *
from migrate import *


meta = MetaData(migrate_engine)
pageviews = Table('pageviews', meta,
                Column('st_id', Integer, Sequence('page_seq_id', optional=True), primary_key=True),
                Column('st_user_agent', String(255), default=''),
                Column('st_url', String(8000), default=''),
                Column('st_spider_date', DateTime, default=''),
                )

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    pageviews.create()
    
def downgrade():
    # Operations to reverse the above upgrade go here.
    pageviews.drop()
