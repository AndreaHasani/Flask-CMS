from flask import (Flask, render_template, request, session, current_app,
                   jsonify, abort, redirect, url_for, Blueprint)
from SCMS.core.models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from SCMS import db
from SCMS.core.users.model import loginForm, registerForm
from SCMS.core.users.util import login_required
import os


users = Blueprint('users', __name__, static_folder=os.path.join(
    current_app.root_path, 'core/static'),
    template_folder=os.path.join(current_app.root_path, 'core/templates'),
    url_prefix='/')


@users.route("/", methods=["GET", "POST"])
def user():
    return render_template("index.html")


@users.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()

    if request.method == "POST":
        code = False
        if form.validate_on_submit():
            user = Users.query.filter_by(username=form.username.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for("users.register"))
                else:
                    code = 401
                    msg = "Wrong Username or Password"
            else:
                code = 401
                msg = "User does not exist"

            if code:
                return jsonify(code=code, message=msg)
        else:
            return jsonify(code=401, message="Validation Error",
                           errors=form.errors)

    return render_template("admin-login.html", form=form)


@users.route("/register", methods=["GET", "POST"])
@login_required('admin', ('testing', 'reader'))
def register():

    current_user.add_role('test')
    result = current_user.remove_role('athor')
    print(current_user.get_roles())
    print(result)
    form = registerForm()

    if request.method == "POST":
        if form.validate_on_submit():
            hashPassword = generate_password_hash(
                form.password.data, method='sha256')
            newUser = Users(username=form.username.data,
                            email=form.email.data, password=hashPassword)
            db.session.add(newUser)
            db.session.commit()
            return jsonify(code=301, message="Registration Succesful")
        else:
            return jsonify(code=401, message="Validation Error",
                           errors=form.errors)

    return render_template("admin-login.html", form=form)


@users.route("/logout", methods=["GET", "POST"])
@login_required(None)
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard/dashboard.html")


# Users Posts
@users.route("/posts/new", methods=["GET", "POST"])
def posts_new():
    return render_template("posts/new.html")

@users.route("/posts/view", methods=["GET", "POST"])
def posts_view():
    return render_template("posts/view.html")


@users.route("/api/posts/new", methods=["POST"])
def posts_new_api():
    data = request.form.get("content", None)
    if data:
        print(data)
        return jsonify(code=200)
    else:
        print("Data empty")
        return jsonify(code=404)



@users.route("/media/view", methods=["GET", "POST"])
def media_view():
    return render_template("media/view.html")

@users.route("/media/upload", methods=["GET", "POST"])
def media_upload():
    return render_template("media/upload.html")

# Users settings
@users.route("/settings/profile", methods=["GET", "POST"])
def settings_profile():
    return render_template("settings/profile.html")
