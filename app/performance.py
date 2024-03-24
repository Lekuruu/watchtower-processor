
from rosu_pp_py import Beatmap, Calculator
from functools import lru_cache
from typing import Optional

import app.session as session
import math

@lru_cache
def beatmap(beatmap_id: int) -> Optional[Beatmap]:
    response = session.requests.get(
        f"https://old.ppy.sh/osu/{beatmap_id}",
        headers={"User-Agent": "watchtower-processor"}
    )

    if not response.ok:
        return None

    if not (file := response.content):
        return None

    return Beatmap(bytes=file)

def calculate_ppv2(beatmap_id: int, mode: int, score: dict) -> float:
    if not (map := beatmap(beatmap_id)):
        return 0.0

    calc = Calculator(
        mode = mode,
        mods = score['mods'],
        n_geki = score['cGeki'],
        n_katu = score['cKatu'],
        n300 = score['c300'],
        n100 = score['c100'],
        n50 = score['c50'],
        n_misses = score['cMiss'],
        combo = score['max_combo'],
        passed_objects = score['total_hits']
    )

    if not (result := calc.performance(map)):
        return 0.0

    if math.isnan(result.pp):
        return 0.0

    if math.isinf(result.pp):
        return 0.0

    return result.pp
