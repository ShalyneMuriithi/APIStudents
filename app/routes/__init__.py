from .read import read_bp
from .create import create_bp
from .update import update_bp
from .delete import delete_bp

def register_blueprints(app):
    app.register_blueprint(read_bp)
    app.register_blueprint(create_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(delete_bp)
