from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_user_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def create_label(db: Session, label: schemas.LabelCreate):
    label_exists = (
        db.query(models.Label).filter(models.Label.label == label.label).first()
    )
    if label_exists:
        return label
    else:
        db_label = models.Label(**label.dict())
        db.add(db_label)
        db.commit()
        db.refresh(db_label)
        return db_label


def get_labels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Label).offset(skip).limit(limit).all()
