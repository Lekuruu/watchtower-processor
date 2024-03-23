
from sqlalchemy.orm import Session
from .wrapper import session_wrapper
from ..objects import DBScore

@session_wrapper
def create(
    score: DBScore,
    session: Session = ...
) -> DBScore:
    session.add(score)
    session.commit()
    return score

@session_wrapper
def by_id(
    score_id: int,
    session: Session = ...
) -> DBScore:
    return (
        session.query(DBScore)
               .filter(DBScore.id == score_id)
               .first()
    )

@session_wrapper
def by_checksum(
    checksum: str,
    session: Session = ...
) -> DBScore:
    return (
        session.query(DBScore)
               .filter(DBScore.checksum == checksum)
               .first()
    )

@session_wrapper
def by_user_id(
    user_id: int,
    session: Session = ...
) -> DBScore:
    return (
        session.query(DBScore)
               .filter(DBScore.user_id == user_id)
               .all()
    )

@session_wrapper
def recent(
    limit: int = 50,
    offset: int = 0,
    session: Session = ...
) -> list[DBScore]:
    return (
        session.query(DBScore)
               .order_by(DBScore.submitted_at.desc())
               .limit(limit)
               .offset(offset)
               .all()
    )
