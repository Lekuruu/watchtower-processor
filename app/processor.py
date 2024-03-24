
from app.data import DBMessage, DBScore
from app.data import messages, scores

import app.session as session

@session.events.register("score")
def process_score(
    checksum: str,
    server: str,
    player: dict,
    score: dict
):
    session.logger.info(
        f"Processing score from {player['name']} on {server} ({checksum})..."
    )
    # TODO

@session.events.register("message")
def process_message(
    server: str,
    sender_name: str,
    sender_id: int,
    message: str,
    target: str
):
    messages.create(
        DBMessage(
            sender_id=sender_id,
            sender_name=sender_name,
            target_name=target,
            server=server,
            message=message
        )
    )
    session.logger.info(
        f"[#spectator-{target}] {target}: {message}"
    )
