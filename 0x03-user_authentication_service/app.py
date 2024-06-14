#!/usr/bin/env python3
"""
A script to handle application routes.
"""
from flask import Flask, jsonify, request, abort
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """
    To handle the default route.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    A method used to handle users.
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = AUTH._db.find_user_by(email=email)
            return jsonify({"message": "email already registered"}), 400
        except NoResultFound:
            user = AUTH.register_user(email, password)
            return jsonify({
                            "email": "{}".format(email),
                            "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    A method to log user into the app.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if (AUTH.valid_login(email, password)):
        new_session = AUTH.create_session(email)
        user = AUTH._db.find_user_by(email=email)
        args = {'session_id': new_session}
        AUTH._db.update_user(user.id, **args)
        res = jsonify({"email": "{}".format(email), "message": "logged in"})
        res.set_cookie("session_id", new_session)
        return res
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
