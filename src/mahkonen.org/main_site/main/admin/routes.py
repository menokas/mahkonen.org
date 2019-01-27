from flask import Blueprint, jsonify

admin = Blueprint('admin', __name__)

@admin.route("/admin")
def about():
    return jsonify('{"status":"GOOD"}')