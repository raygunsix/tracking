"""Setup the tracking application"""
import logging
import os.path

from tracking import model
from tracking.config.environment import load_environment
from tracking.model import *

from fixture import SQLAlchemyFixture
from fixture.style import NamedDataStyle
from tracking.datasets import PageviewsData

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup tracking here"""
    load_environment(conf.global_conf, conf.local_conf)

    filename = os.path.split(conf.filename)[-1]

    if filename == 'test.ini':
        
        # Permanently drop any existing tables
        
        log.info("Dropping existing tables...")
        
        meta.Base.metadata.drop_all(bind=meta.engine, checkfirst=True)

    log.info("Creating tables...")

    # Create the tables if they don't already exist
    meta.Base.metadata.create_all(bind=meta.engine)
    
    log.info("Successfully set up.")
    
    if filename == 'development.ini':
    
        # load sample data during setup-app
    
        db = SQLAlchemyFixture(
                env=model, style=NamedDataStyle(),
                engine=meta.engine)
            
        data = db.data(KeyphrasesData)
        log.info("Loading sample data...")
        data.setup()
        
    log.info("Successfully set up.")
