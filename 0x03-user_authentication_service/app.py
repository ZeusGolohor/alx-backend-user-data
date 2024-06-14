#!/usr/bin/env python3
"""
A script to handle application routes.
"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
