from sqlalchemy import *
from migrate import *
import migrate.changeset

from sqlalchemy.ext.declarative import declarative_base

meta = MetaData(migrate_engine)
Base = declarative_base(metadata=meta)

class PageviewsNew(Base):
    __tablename__ = "pageviews"

    id = Column(Integer, Sequence('page_seq_id', optional=True), primary_key=True)
    user_agent = Column(String(255), default='')
    url = Column(String(8000), default='')
    spider_date = Column(DateTime, default='')

class PageviewsOld(Base):
    __tablename__ = "pageviews"
    __table_args__ = (
            {'useexisting':True}
            )

    st_id = Column(Integer, Sequence('page_seq_id', optional=True), primary_key=True)
    user_agent = Column(String(255), default='')
    url = Column(String(8000), default='')
    spider_date = Column(DateTime, default='')

def upgrade():
    # Upgrade operations go here.
    PageviewsOld.__table__.c.st_id.alter(name='id')

def downgrade():
    # Operations to reverse the above upgrade go here.
    PageviewsNew.__table__.c.id.alter(name='st_id')
