"""create game routes"""
import os
from flask import Blueprint, send_file, send_from_directory, current_app, jsonify

frontend = Blueprint(
    "frontend",
    __name__,
)


@frontend.route("/")
def root():
    """returns index.html from svelte frontend"""
    return send_from_directory("static/build/", "index.html")


@frontend.route("/<path:path>")
def home(path):
    """returns svelte frontend"""

    return send_from_directory("static/build/", path)


@frontend.route("/api/assets/<arg_dir>/<arg_name>")
def get_assset(arg_dir, arg_name):
    """returns svelte frontend"""
    image_path = f"static/assets/{arg_dir}/{arg_name}"
    content_type = "image/jpeg"

    image_path = os.path.abspath(image_path)

    return send_file(image_path, mimetype=content_type)


@frontend.route("/api/avatars")
def get_avatar_pathes():
    """get all avatar pathes"""

    # Get all files in the directory
    avatars = [
        "avatars/" + f
        for f in os.listdir(current_app.config["AVATAR_DIR"])
        if os.path.isfile(os.path.join(current_app.config["AVATAR_DIR"], f))
    ]
    return jsonify(avatars)
