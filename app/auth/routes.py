from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, unset_jwt_cookies
)
from app.models import db, User
from app import bcrypt
from datetime import  timedelta
from app import blacklist
from flask_jwt_extended import get_jwt
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401  #If user doesn't exist or password is wrong, return an error

    access_token = create_access_token(identity=str(user.id) , expires_delta=timedelta(minutes=30))

    refresh_token = create_refresh_token(identity=str(user.id) , expires_delta=timedelta(minutes=60) )
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200

@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = str(get_jwt_identity())
    user = User.query.get(int(user_id))
    return jsonify(username=user.username), 200

@auth_bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "Logout successful"})
   
# Get the unique ID of the current token
    jti = get_jwt()["jti"]

    # Add the token's ID to the blacklist so it can't be used again
    blacklist.add(jti)
    response = jsonify({"msg": "Logout successful"})
    

    return response, 200
