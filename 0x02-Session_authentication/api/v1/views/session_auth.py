#!/usr/bin/env python3
"""
Model for session views
"""
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """
    Used to login into the app.
    """
    email = request.form.get("email")
    if (email is None) or (len(email) == 0):
        error_response = jsonify({"error": "email missing"})
        return make_response(error_response, 400)
    password = request.form.get("password")
    if (password is None) or (len(password) == 0):
        error_response = jsonify({"error": "password missing"})
        return make_response(error_response, 400)
    users = User.search({"email": email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            res = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            res.set_cookie(session_name, session_id)
            return res
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    """
    A method used to logout of the application.
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
