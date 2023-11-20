"""create game routes"""
from flask import Blueprint, jsonify, request
from src.models.game import Team
from src.data import current_team, current_game

create_teams = Blueprint(
    "teams",
    __name__,
)


@create_teams.route("/api/update_current_team", methods=["POST"])
def update_current_team():
    """create a team"""
    current_team.name = request.form.get("name")
    current_team.name_shortcut = request.form.get("shortcut")
    current_team.avatar_url = request.form.get("avatar_url")
    return jsonify(current_team.to_json())


@create_teams.route("/api/deleteTeam", methods=["GET"])
def delete_team():
    """delete team"""
    team_idx = int(request.args.get("idx", -1))

    if 0 <= team_idx < len(current_game.teams):
        current_game.teams.pop(team_idx)
        current_game.current_turn_team = -1
    return jsonify(True)


@create_teams.route("/api/get_current_team")
def get_current_team():
    """create a team"""

    is_show = (
        not (
            current_team.name.strip() == ""
            and current_team.name_shortcut.strip() == ""
            and current_team.avatar_url.strip() == ""
        )
        and len(current_game.teams) < 4
    )
    ret = {"team": current_team.to_json(), "isShow": is_show}
    return jsonify(ret)


@create_teams.route("/api/add_team", methods=["POST"])
def add_team():
    """create a team"""

    if len(current_game.teams) >= 4:
        return jsonify("full")

    team = Team()
    team.name = request.form.get("name")
    team.name_shortcut = request.form.get("shortcut")
    team.avatar_url = request.form.get("avatar_url")
    current_game.add_team(team)

    # recreate team
    current_team.reset()
    return jsonify("ok")
