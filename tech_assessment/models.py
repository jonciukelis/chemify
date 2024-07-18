import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, ForeignKey, Enum
from sqlalchemy.orm import relationship

from .db import Base

class Status(enum.Enum):
    PENDING = 'Pending'
    DOING = 'Doing'
    BLOCKED = 'Blocked'
    DONE = 'Done'

task_labels = Table(
    "task_labels",
    Base.metadata,
    Column("task_id", ForeignKey("tasks.id"), primary_key=True),
    Column("label_id", ForeignKey("labels.label"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    tasks = relationship("Task", back_populates="owner")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    status = Column(Enum(Status))
    archived = Column(Boolean, default=False)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    labels = relationship("Label", secondary=task_labels, back_populates="tasks")
    owner = relationship("User", back_populates="tasks")


class Label(Base):
    __tablename__ = "labels"

    label = Column(String, primary_key=True, index=True)
    tasks = relationship("Task", secondary=task_labels, back_populates="labels")
