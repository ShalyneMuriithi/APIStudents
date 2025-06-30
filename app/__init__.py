
from flask import Flask , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

bcrypt = Bcrypt()
blacklist = set()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config["JWT_BLACKLIST_ENABLED"] = True
    app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]



    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"msg": "Invalid token"}), 401

    #Token is missing (no Authorization header)
    @jwt.unauthorized_loader
    def missing_token_callback(error):  #(error)the token is invalid
        return jsonify({"msg": "Missing token"}), 401

# Token is expired
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):  #decoding info from the token
        return jsonify({"msg": "Token has expired"}), 401

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        return jwt_payload["jti"] in blacklist  #if token's ID is in the blacklist.its is revoked.
    #jti is JWT ID , a unique ID for every token.
    return app

