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


@create_teams.route("/api/get_current_team")
def get_current_team():
    """create a team"""
    return jsonify(current_team.to_json())


@create_teams.route("/api/add_team", methods=["POST"])
def add_team():
    """create a team"""

    team = Team()
    team.name = request.form.get("name")
    team.name_shortcut = request.form.get("shortcut")
    team.avatar_url = request.form.get("avatar_url")
    current_game.add_team(team)

    # recreate team
    current_team.reset()
    return jsonify("ok")
