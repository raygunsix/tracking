"""Setup the tracking application"""
import logging

from tracking.config.environment import load_environment
from tracking.model import meta

from tracking import model
from fixture import SQLAlchemyFixture
from fixture.style import NamedDataStyle
from tracking.datasets import PageviewsData

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup tracking here"""
    load_environment(conf.global_conf, conf.local_conf)

    log.info("Creating tables")
    
    # Create the tables if they don't already exist
    meta.metadata.create_all(bind=meta.engine)
    
    log.info("Successfully setup")

    # load some initial data during setup-app :
    
    db = SQLAlchemyFixture(
            env=model, style=NamedDataStyle(),
            engine=meta.engine)
            
    data = db.data(PageviewsData)
    log.info("Inserting initial data")
    data.setup()
    log.info("Done")
