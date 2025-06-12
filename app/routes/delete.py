from flask import Blueprint, jsonify
from app.models import Learners
from app import db

delete_bp = Blueprint('delete', __name__, url_prefix='/learners')

@delete_bp.route('/<int:id>', methods=['DELETE'])
def delete_learner(id):
    learner = Learners.query.get_or_404(id)
    db.session.delete(learner)
    db.session.commit()
    return jsonify({"message": "Learner deleted"})
