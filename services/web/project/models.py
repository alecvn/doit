from datetime import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from project import db


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


class User(TimestampMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    slack_address = db.Column(db.String(128), unique=True, nullable=False)
    slack_id = db.Column(db.String(128), unique=True, nullable=False)
    task_completed_emoji = db.Column(db.String(128))
    reactions = db.relationship("Reaction", back_populates="user")

    def __init__(self, slack_address, slack_id):
        self.slack_address = slack_address
        self.slack_id = slack_id


class Task(TimestampMixin, db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    ts = db.Column(db.String(128), nullable=False)
    channel = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    reactions = db.relationship("Reaction", back_populates="task")
    # completed = db.Column(db.Boolean)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # user = db.relationship("User", back_populates="tasks")


class Reaction(TimestampMixin, db.Model):
    __tablename__ = "reactions"

    id = db.Column(db.Integer, primary_key=True)
    emoji = db.Column(db.String(128))
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    task = db.relationship("Task", back_populates="reactions")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="reactions")


def get_or_create(session, model, defaults=None, **kwargs):
    """
    Get or create a model instance while preserving integrity.
    """
    try:
        return session.query(model).filter_by(**kwargs).one(), False

    except NoResultFound:
        if defaults is not None:
            kwargs.update(defaults)
        try:
            with session.begin_nested():
                instance = model(**kwargs)
                session.add(instance)
                return instance, True
        except IntegrityError:
            return session.query(model).filter_by(**kwargs).one(), False
