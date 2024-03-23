
import app.session as session

@session.events.register("score")
def process_score(
    checksum: str,
    server: str,
    player: dict,
    score: dict
):
    ... # TODO

@session.events.register("message")
def process_message(
    server: str,
    sender: str,
    message: str,
    target: str
):
    ... # TODO
