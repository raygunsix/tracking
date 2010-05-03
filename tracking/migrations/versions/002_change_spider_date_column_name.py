from sqlalchemy import *
from migrate import *

meta = MetaData(migrate_engine)

col = Column('st_spider_date')

def upgrade():
    # Upgrade operations go here. Don't create your own engine; use the engine
    # named 'migrate_engine' imported from migrate.
    col.alter(name='spider_date')

def downgrade():
    # Operations to reverse the above upgrade go here.
    col.alter(name='st_spider_date')
