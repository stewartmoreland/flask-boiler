#! /usr/bin/env python

from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import QueryableAttribute

__session_options = {'autocommit':True}
__engine_options = {'isolation_level':'READ COMMITTED'}

db = SQLAlchemy(engine_options= __engine_options, session_options=__session_options)


def persist(model):
    """ Persist model to the database

    Args:
        model (object): Database model

    Returns:
        model: Database model object with the newly inserted id 
    """
    db.session.begin()
    try:
        db.session.add(model)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return model
