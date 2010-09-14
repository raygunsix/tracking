from sqlalchemy import *
from migrate import *

from sqlalchemy.ext.declarative import declarative_base

meta = MetaData(migrate_engine)
Base = declarative_base(metadata=meta)

class Pageviews(Base):
    __tablename__ = "pageviews"

    st_id = Column(Integer, Sequence('page_seq_id', optional=True), primary_key=True)
    st_user_agent = Column(String(255), default='')
    st_url = Column(String(8000), default='')
    st_spider_date = Column(DateTime, default='')

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    Pageviews.__table__.create()
    
def downgrade():
    # Operations to reverse the above upgrade go here.
    Pageviews.__table__.drop()
