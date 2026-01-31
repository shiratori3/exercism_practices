import copy


def tally(rows: list[str]) -> list[str]:
    res = dict()
    default_score = dict.fromkeys(["MP", "W", "D", "L", "P"], 0)
    for row in rows:
        team1, team2, result1 = row.split(";")
        result2 = "loss" if result1 == "win" \
            else "win" if result1 == "loss" else "draw"
        for team, result in [(team1, result1), (team2, result2)]:
            res.setdefault(team, copy.deepcopy(default_score))
            score_cal(res[team], result)

    sorted_team = sorted(res.keys(), key=lambda team: (-res[team]["P"], team))
    output = ["Team                           | MP |  W |  D |  L |  P"]
    for team in sorted_team:
        output.append(
            "{: <30} | {: >2} | {: >2} | {: >2} | {: >2} | {: >2}".format(
                team, res[team]["MP"], res[team]["W"],
                res[team]["D"], res[team]["L"], res[team]["P"]
            ))
    return output


def score_cal(score: dict[str, int], result: str) -> None:
    score["MP"] += 1
    if result == "win":
        score["W"] += 1
        score["P"] += 3
    elif result == "draw":
        score["D"] += 1
        score["P"] += 1
    else:
        score["L"] += 1
