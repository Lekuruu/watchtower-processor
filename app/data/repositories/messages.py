
from sqlalchemy.orm import Session
from .wrapper import session_wrapper
from ..objects import DBMessage

@session_wrapper
def create(
    message: DBMessage,
    session: Session = ...
) -> DBMessage:
    session.add(message)
    session.commit()
    return message

@session_wrapper
def by_id(
    message_id: int,
    session: Session = ...
) -> DBMessage:
    return (
        session.query(DBMessage)
               .filter(DBMessage.id == message_id)
               .first()
    )

@session_wrapper
def by_sender_id(
    sender_id: int,
    session: Session = ...
) -> DBMessage:
    return (
        session.query(DBMessage)
               .filter(DBMessage.sender_id == sender_id)
               .all()
    )

@session_wrapper
def by_sender_name(
    sender_name: str,
    session: Session = ...
) -> DBMessage:
    return (
        session.query(DBMessage)
               .filter(DBMessage.sender_name == sender_name)
               .all()
    )

@session_wrapper
def by_target_name(
    target_name: str,
    session: Session = ...
) -> DBMessage:
    return (
        session.query(DBMessage)
               .filter(DBMessage.target_name == target_name)
               .all()
    )

@session_wrapper
def recent(
    limit: int = 50,
    offset: int = 0,
    session: Session = ...
) -> DBMessage:
    return (
        session.query(DBMessage)
               .order_by(DBMessage.created_at.desc())
               .limit(limit)
               .offset(offset)
               .all()
    )
