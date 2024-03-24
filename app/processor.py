
from app.data import DBMessage, DBScore
from app.data import messages, scores

import app.performance as performance
import app.session as session
import json

@session.events.register("score")
def process_score(
    checksum: str,
    server: str,
    player: str,
    score: str
) -> None:
    player = json.loads(player)
    score = json.loads(score)

    pp = performance.calculate_ppv2(
        player['status']['beatmap_id'],
        player['status']['mode'],
        score
    )

    score = scores.create(
        DBScore(
            user_id=player['id'],
            user_name=player['name'],
            user_country=player['country'],
            server=server,
            beatmap_id=player['status']['beatmap_id'],
            beatmap_text=player['status']['text'],
            beatmap_checksum=player['status']['checksum'],
            checksum=checksum,
            mode=player['status']['mode'],
            pp=pp,
            acc=score['accuracy'],
            total_score=score['total_score'],
            max_combo=score['max_combo'],
            mods=score['mods'],
            perfect=score['perfect'],
            passed=score['passed'],
            length=score['length'],
            grade=score['grade'],
            c300=score['c300'],
            c100=score['c100'],
            c50=score['c50'],
            cgeki=score['cGeki'],
            ckatu=score['cKatu'],
            cmiss=score['cMiss'],
            replay_filename=score['filename_safe']
        )
    )

    session.logger.info(
        f"Processed score from {player['name']} on {server} ({checksum})."
    )

    # TODO: Save replay to storage

@session.events.register("message")
def process_message(
    server: str,
    sender_name: str,
    sender_id: int,
    message: str,
    target: str
) -> None:
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
