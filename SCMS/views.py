from flask import Flask, render_template, request, session, jsonify, abort, redirect, url_for, Blueprint, current_app, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
import os
# from SCMS import application, db, login_manager

# main = Blueprint('main', __name__, static_folder=os.path.join(
#     current_app.root_path, 'themes/static'), template_folder=os.path.join(
#     current_app.root_path, 'themes/templates'))


main = Blueprint('main', __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/admin/static/<path:filename>", methods=["GET", "POST"])
def admin(filename):
    return send_from_directory(current_app.config['ADMIN_STATIC'],
                               filename=filename)
